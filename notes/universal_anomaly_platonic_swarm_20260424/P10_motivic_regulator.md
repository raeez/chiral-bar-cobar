# P10: Motivic and Regulator Surface

Date: 2026-04-24.

Owned file:

- `notes/universal_anomaly_platonic_swarm_20260424/P10_motivic_regulator.md`

Read-only target surface:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`

No target TeX file was edited.

## Verdict

There is no currently proved motivic lift of the Atiyah--Connes class.

The present manuscript has already demoted the motivic claims to
conjectural status, which is correct. The remaining mathematical
problem is sharper: the displayed motivic group is still the wrong
direct regulator home for the class
\[
  \alpha_X=[m_3,B^{(2)}]_X\in H^2(X,\Omega_X^1)=H^{1,2}(X).
\]

The direct motivic candidate is not
\[
  H^3_{\mathcal M}(X,\Qbb(2))=\mathrm{CH}^2(X,1)_{\Qbb}.
\]
That group has a regulator to \(H^3_{\mathcal D}(X,\Qbb(2))\). Its
Deligne target is controlled by \(F^2H^3(X)\) and by \(H^2(X)/F^2\);
it does not canonically output an \(H^{1,2}\) vector.

The correct direct Abel--Jacobi home for an \(H^{1,2}\) obstruction is
codimension-two motivic cohomology in degree four:
\[
  H^4_{\mathcal M}(X,\Qbb(2))
  =
  \mathrm{CH}^2(X)_{\Qbb},
\]
with homologically trivial part mapping by the Beilinson--Deligne
regulator to
\[
  J^2(X)_{\Qbb}
  =
  H^3(X,\Cbb)/
  \bigl(F^2H^3(X,\Cbb)+H^3(X,\Qbb(2))\bigr)
  \subset
  H^4_{\mathcal D}(X,\Qbb(2)).
\]
The \(H^{1,2}(X)\) component is the tangent or quotient component of
this intermediate Jacobian:
\[
  T_0J^2(X)\simeq H^3(X,\Cbb)/F^2H^3(X,\Cbb)
  \simeq H^{1,2}(X)\oplus H^{0,3}(X).
\]
After fixing the Calabi--Yau volume and primitive projection, the
desired obstruction is an infinitesimal Abel--Jacobi/normal-function
class in the \(H^{1,2}\) summand. It is not a literal regulator value
landing in a standalone Hodge summand.

This is still deep. It says the motivic frontier should be a normal
function attached to a codimension-two cycle whose infinitesimal
invariant is the Atiyah--Connes obstruction.

## Sources and local anchors

Local anchors:

- Motivic subsection:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:536`.
- Current \(H^3_{\mathcal M}(X,\Qbb(2))\) claim:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:541`.
- Torsion-graph representative:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:546`.
- Vanishing at motivic level:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:553`.
- Current \(\ell\)-adic realization:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:562`.
- Tsygan--Shoikhet motivic block:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:616`.
- Explicit representative in \(\mathrm{CH}^3(X,1)\):
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:637`.
- Five-faces table:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:722`.
- P01 fixed the cyclic/HKR target:
  `notes/universal_anomaly_platonic_swarm_20260424/P01_cyclic_hkr_core.md:35`.
- A1 already flagged the motivic lift as unproved:
  `notes/universal_anomaly_attack_heal_20260424/A1_cocycle_hodge.md:105`.

Primary-source anchors checked:

- Bloch, `Algebraic cycles and higher K-theory`, Adv. Math. 61
  (1986), DOI `10.1016/0001-8708(86)90081-2`; the paper is the
  source for \(\mathrm{CH}^p(X,n)\).
- Beilinson, `Higher regulators and values of L-functions`, 1984/1985,
  already cited in the target bibliography.
- Beilinson, `Notes on absolute Hodge cohomology`, 1985/1986, already
  cited in the target bibliography.
- Esnault--Viehweg, `Deligne--Beilinson cohomology`, 1988, already
  cited in the target bibliography; the notes record the exact sequence
  with intermediate Jacobian and identify the homologically trivial
  cycle map with Abel--Jacobi.
- Green, `Griffiths' infinitesimal invariant and the Abel--Jacobi map`,
  JDG 29 (1989), Theorem 2.1; this is a model for infinitesimal
  normal-function invariants, not a construction of the cycle needed
  here.

Web source checks used for bibliographic anchoring:

- Bloch 1986 DOI page:
  `https://www.sciencedirect.com/science/article/pii/0001870886900812`.
- Esnault--Viehweg PDF mirror:
  `https://ncatlab.org/nlab/files/EsnaultViehweg-DeligneBeilinsonCohomology.pdf`.

## Attacks

### Critical 1: \(H^3_{\mathcal M}(X,\Qbb(2))\) is the wrong direct home

Bloch's convention gives
\[
  H^i_{\mathcal M}(X,\Qbb(j))
  \cong
  \mathrm{CH}^j(X,2j-i)_{\Qbb}.
\]
Thus
\[
  H^3_{\mathcal M}(X,\Qbb(2))
  =
  \mathrm{CH}^2(X,1)_{\Qbb}.
\]
Its Beilinson regulator lands in
\[
  H^3_{\mathcal D}(X,\Qbb(2)).
\]
For a smooth projective complex variety the relevant exact sequence is
\[
0\to
 {H^2(X,\Cbb)\over F^2H^2(X,\Cbb)+H^2(X,\Qbb(2))}
\to
H^3_{\mathcal D}(X,\Qbb(2))
\to
H^3(X,\Qbb(2))\cap F^2H^3(X,\Cbb)
\to 0 .
\]
On a Calabi--Yau threefold,
\[
  F^2H^3=H^{3,0}\oplus H^{2,1}.
\]
The class \(\alpha_X\) sits in \(H^{1,2}=H^2(X,\Omega^1_X)\). It is
therefore not a canonical component of this regulator target.

The only way to keep \(H^3_{\mathcal M}(X,\Qbb(2))\) is to change the
claim: it could carry a dual or conjugate \(F^2\)-class, or a
transgression whose boundary has an \(H^{1,2}\) shadow after extra
duality. That is not the current statement.

### Critical 2: the correct direct target is \(H^4_{\mathcal D}(X,\Qbb(2))\)

For codimension-two cycles,
\[
  H^4_{\mathcal M}(X,\Qbb(2))
  =
  \mathrm{CH}^2(X)_{\Qbb}
\]
maps to
\[
  H^4_{\mathcal D}(X,\Qbb(2)).
\]
The Deligne exact sequence is
\[
0\to
J^2(X)_{\Qbb}
\to
H^4_{\mathcal D}(X,\Qbb(2))
\to
\mathrm{Hdg}^2(X)_{\Qbb}
\to 0,
\]
where
\[
  J^2(X)_{\Qbb}
  =
  H^3(X,\Cbb)/
  \bigl(F^2H^3(X,\Cbb)+H^3(X,\Qbb(2))\bigr).
\]
A homologically trivial codimension-two cycle maps to \(J^2(X)\) by
Abel--Jacobi. This is the only standard regulator surface whose
holomorphic tangent contains
\[
  H^3/F^2H^3\simeq H^{1,2}\oplus H^{0,3}.
\]
Thus the correct motivic lift, if it exists, is a homologically
trivial codimension-two cycle or a family of such cycles whose
normal-function infinitesimal invariant is \(\alpha_X\).

### Critical 3: the torsion graph of the Chern connection is not a cycle

The current representative
\[
  [\Gamma_\nabla]\in z^2(X,1)_{\Qbb}
\]
is not constructed.

There are two independent failures.

First, a Chern connection on a K\"ahler tangent bundle is torsion-free in
the relevant differential-geometric sense. On a Calabi--Yau main
stratum this cannot be the source of a generally nonzero obstruction.

Second, even a nonzero differential-geometric graph is not by itself an
algebraic cycle in \(X\times\Delta^1\). A Bloch higher-Chow cycle must
meet the faces properly and have algebraic boundary conditions. The
relative K\"ahler cone is not an algebraic simplex, and the graph of a
connection tensor is not a codimension-two algebraic subvariety of
\(X\times\Delta^1\).

The torsion-graph sentence should be removed from any theorem surface.
At most it can be kept as a heuristic for what a future cycle should
imitate.

### Critical 4: the explicit \(\mathrm{CH}^3(X,1)\) representative has the wrong bidegree

The current later representative is
\[
  [\Gamma_\nabla\cup c_1(\Omega_X^1)]
  \in
  \mathrm{CH}^3(X,1)_{\Qbb}.
\]
But
\[
  \mathrm{CH}^3(X,1)_{\Qbb}
  =
  H^5_{\mathcal M}(X,\Qbb(3)),
\]
not \(H^3_{\mathcal M}(X,\Qbb(2))\), and not the Abel--Jacobi home
\(H^4_{\mathcal M}(X,\Qbb(2))\).

Worse, on a Calabi--Yau threefold
\[
  c_1(\Omega_X^1)=c_1(K_X)=0
\]
in rational Chow/cohomology under the chosen trivialisation of the
canonical bundle. This product cannot represent the expected nonzero
quintic obstruction.

### Serious 1: \(B^{(2)}\) has no motivic class yet

The manuscript states a motivic class
\[
  [B^{(2)}]^{\mathcal M}_X\in H^2_{\mathcal M}(X,\Qbb(1))
  \cong \mathrm{Pic}(X)_{\Qbb}.
\]
This is unsupported. Ordinary Connes \(B\) is an operator in a mixed
complex. A motivic class in \(\mathrm{Pic}(X)\) is a line bundle.
Transporting an \(S^1\)-operator on cyclic chains to a Picard class
requires a determinant, orientation, or Chern-class construction which
has not been supplied.

The assertion that \(B^{(2)}\) becomes cup-product with
\(c_1(\Omega_X^1)\) is also incompatible with the Calabi--Yau target:
if it were literally \(c_1(\Omega_X^1)\), it would vanish on the main
stratum and could not generate the nonzero obstruction the paper wants.

### Serious 2: no regulator injectivity survives

No general injectivity theorem is available for the regulator on
\(\mathrm{CH}^2(X)_{\mathrm{hom},\Qbb}\), on
\(\mathrm{CH}^2(X,1)_{\Qbb}\), or on the mixed motivic subspace needed
here. Such injectivity belongs to Bloch--Beilinson/Beilinson--Bloch--
Kato type conjectures, or to special cases with additional structure.

The only unconditional implication is
\[
  Z_\alpha=0 \text{ in motivic cohomology}
  \quad\Rightarrow\quad
  r_{\mathcal D}(Z_\alpha)=0
  \quad\Rightarrow\quad
  \alpha_X=0
\]
after the regulator comparison has been proved.

The converse
\[
  \alpha_X=0 \Rightarrow Z_\alpha=0
\]
is conjectural and requires regulator injectivity on the exact
submotive generated by \(Z_\alpha\).

### Serious 3: the \(\ell\)-adic realization is shifted

If one uses \(H^3_{\mathcal M}(X,\Qbb(2))=\mathrm{CH}^2(X,1)\), then an
\(\ell\)-adic regulator may land in
\[
  H^3_{\mathrm{et}}(X_{\bar k},\Qbb_\ell(2))
\]
or its arithmetic variant.

But for the corrected codimension-two Abel--Jacobi lift, the
homologically trivial cycle has an arithmetic Abel--Jacobi class
\[
  AJ_\ell(Z_\alpha)
  \in
  H^1\!\left(k,H^3_{\mathrm{et}}(X_{\bar k},\Qbb_\ell(2))\right)
\]
when \(X\) is defined over a number field \(k\). The plain
\(H^3_{\mathrm{et}}(X,\Qbb_\ell(2))\) line belongs to the wrong
motivic degree.

### Moderate 1: Green 1989 is being used too strongly

Green's infinitesimal invariant gives a way to read the derivative of
an Abel--Jacobi normal function. It does not construct the algebraic
cycle, prove that a Chern-connection graph is algebraic, or prove that
the regulator of that graph equals the cyclic-skew Atiyah--Connes
projection.

The correct use of Green 1989 is downstream:

1. construct a codimension-two cycle \(Z_\alpha\);
2. form its normal function \(\nu_{Z_\alpha}\);
3. compute the infinitesimal invariant \(\delta\nu_{Z_\alpha}\);
4. prove that the primitive \(H^{1,2}\) component is \(\alpha_X\).

## The corrected motivic surface

### The direct Abel--Jacobi formulation

For a smooth projective Calabi--Yau threefold \(X/\Cbb\), a direct
motivic lift of \(\alpha_X\) should be:
\[
  Z_\alpha(X)\in
  \mathrm{CH}^2(X)_{\mathrm{hom},\Qbb}
  =
  H^4_{\mathcal M}(X,\Qbb(2))_{\mathrm{hom}},
\]
with Deligne regulator
\[
  r_{\mathcal D}(Z_\alpha)
  =
  AJ(Z_\alpha)
  \in
  J^2(X)_{\Qbb}
  \subset
  H^4_{\mathcal D}(X,\Qbb(2)).
\]
The comparison with the Atiyah--Connes class is not equality in
Deligne cohomology. It is equality of the infinitesimal invariant:
\[
  \delta AJ(Z_\alpha)
  =
  \alpha_X
  \quad\text{in}\quad
  H^2(X,\Omega_X^1)
\]
after the chosen primitive projection and the fixed Calabi--Yau volume
normalisation.

### The relative version

The stronger and more natural statement is relative. Let
\[
  \pi:\mathcal X\to \mathcal B^\circ
\]
be the family over the derived CY/chiral-specialisation base used by
P05. A motivic lift should be a relative homologically trivial
codimension-two cycle
\[
  \mathcal Z_\alpha\in
  \mathrm{CH}^2(\mathcal X/\mathcal B^\circ)_{\mathrm{hom},\Qbb}
\]
or a class in the corresponding relative motivic cohomology
\[
  H^4_{\mathcal M}(\mathcal X/\mathcal B^\circ,\Qbb(2)).
\]
Its normal function
\[
  \nu_\alpha:\mathcal B^\circ\to J^2(\mathcal X/\mathcal B^\circ)
\]
should satisfy Griffiths transversality and have infinitesimal
invariant
\[
  \nabla\nu_\alpha
  =
  \alpha_{\mathrm{AC}}
  \in
  H^0\!\left(\mathcal B^\circ,R^2\pi_*\Omega^1_{\mathcal X/\mathcal B}\right)
\]
after projecting away the \(H^{0,3}\) component.

This is the platonic motivic form of the paper.

### The secondary \(CH^2(X,1)\) formulation

\(\mathrm{CH}^2(X,1)\) may still enter, but only as a secondary
transgression:
\[
  \widetilde Z_\alpha\in \mathrm{CH}^2(X,1)_{\Qbb},
  \qquad
  r_{\mathcal D}(\widetilde Z_\alpha)\in H^3_{\mathcal D}(X,\Qbb(2)).
\]
Its regulator can naturally see \(F^2H^3=H^{3,0}\oplus H^{2,1}\), so it
could encode the Serre-dual or conjugate partner of \(\alpha_X\), not
\(\alpha_X\) itself. A paper may use this lane only after writing the
duality map
\[
  H^{2,1}(X)\longleftrightarrow H^{1,2}(X)^\vee
\]
and the transgression from \(H^3_{\mathcal D}\) to the Abel--Jacobi
tangent of \(H^4_{\mathcal D}\).

## Platonic motivic conjecture

```tex
\begin{conjecture}[Motivic Atiyah--Connes normal function]
\label{conj:motivic-atiyah-connes-normal-function}
Let \(X/\Cbb\) be a smooth projective Calabi--Yau threefold equipped
with a Calabi--Yau volume form and a cyclic dg enhancement of
\(\Perf(X)\). Suppose the Atiyah--Connes HKR class
\[
  \alpha_X=[m_3,B^{(2)}]_X\in H^2(X,\Omega_X^1)
\]
has been constructed with fixed cyclic and HKR normalisations.
Then there is a functorial homologically trivial codimension-two
cycle
\[
  Z_\alpha(X)\in \mathrm{CH}^2(X)_{\mathrm{hom},\Qbb}
  =
  H^4_{\mathcal M}(X,\Qbb(2))_{\mathrm{hom}}
\]
whose Beilinson--Deligne regulator
\[
  r_{\mathcal D}(Z_\alpha)=AJ(Z_\alpha)\in J^2(X)_{\Qbb}
  \subset H^4_{\mathcal D}(X,\Qbb(2))
\]
has infinitesimal Abel--Jacobi invariant equal to the primitive
Atiyah--Connes class:
\[
  \delta AJ(Z_\alpha)=\alpha_X
  \quad\text{in}\quad
  H^2(X,\Omega_X^1).
\]
Equivalently, in absolute Hodge realisation,
\[
  r_{\mathcal H}(Z_\alpha)\in
  \operatorname{Ext}^1_{\mathrm{MHS}}
  \bigl(\Qbb(0),H^3(X,\Qbb(2))\bigr)
\]
maps to \(\alpha_X\) under the tangent projection
\[
  \operatorname{Ext}^1_{\mathrm{MHS}}
  \bigl(\Qbb(0),H^3(X,\Qbb(2))\bigr)
  \to H^3(X,\Cbb)/F^2H^3(X,\Cbb)
  \to H^{1,2}(X).
\]
\end{conjecture}
```

Relative strengthening:

```tex
\begin{conjecture}[Relative motivic Atiyah--Connes class]
For the universal Calabi--Yau family
\(\pi:\mathcal X\to\mathcal B^\circ\), there exists a relative
homologically trivial codimension-two motivic class
\[
  \mathcal Z_\alpha\in
  H^4_{\mathcal M}(\mathcal X/\mathcal B^\circ,\Qbb(2))_{\mathrm{hom}}
\]
whose normal function \(\nu_\alpha\) has infinitesimal invariant
\[
  \delta\nu_\alpha=\alpha_{\mathrm{AC}}
  \in
  H^0(\mathcal B^\circ,R^2\pi_*\Omega^1_{\mathcal X/\mathcal B}).
\]
\end{conjecture}
```

Vanishing statement, with the only honest implication separated:

```tex
\begin{corollary}[Motivic vanishing, conditional on construction and injectivity]
Assume Conjecture~\ref{conj:motivic-atiyah-connes-normal-function}.
If \(Z_\alpha(X)=0\) in
\(\mathrm{CH}^2(X)_{\mathrm{hom},\Qbb}\), then \(\alpha_X=0\).
Conversely, if the Abel--Jacobi/regulator map is injective on the
subspace generated by \(Z_\alpha(X)\), then \(\alpha_X=0\) implies
\(Z_\alpha(X)=0\).
\end{corollary}
```

## Proof obligations

1. Define \(B^{(2)}\) as an operator in a fixed cyclic or negative
   cyclic total complex, including homological/cohomological degree,
   signs, trace degree, and the framed-\(E_2\) or \(S^1\)-transport.

2. Construct the HKR polyvector class
   \[
     \beta_X\in H^2(X,\wedge^2T_X)
   \]
   and prove
   \[
     \alpha_X=\iota_{\beta_X}\Omega_X\in H^2(X,\Omega_X^1)
   \]
   independently of the connection representative.

3. Construct an algebraic codimension-two cycle
   \[
     Z_\alpha(X)\in\mathrm{CH}^2(X)_{\mathrm{hom},\Qbb}.
   \]
   It cannot be the graph of a Chern-connection torsion tensor unless
   that graph is replaced by an actual algebraic cycle satisfying the
   Bloch boundary and proper-face conditions.

4. Prove the cycle is homologically trivial. Otherwise its Deligne
   regulator has a Hodge-class component in \(\mathrm{Hdg}^2(X)\), not
   the desired Abel--Jacobi component.

5. Compute the Beilinson--Deligne regulator by currents, Deligne
   complexes, or mixed Hodge structures and identify the image in
   \[
     J^2(X)=H^3/(F^2+H^3_{\Qbb}(2)).
   \]

6. Compute the infinitesimal invariant of the normal function and prove
   the primitive \(H^{1,2}\) component is exactly \(\alpha_X\), including
   the \(2\pi i\), sign, and Calabi--Yau volume normalisation.

7. Remove the \(H^{0,3}\) ambiguity. Either prove the normal function is
   primitive, or define the projection that kills the volume-direction
   component.

8. If a \(CH^2(X,1)\) class is retained, prove the transgression from
   \(H^3_{\mathcal D}(X,\Qbb(2))\) to the Abel--Jacobi tangent and show
   it lands in the dual or conjugate of \(\alpha_X\). Do not call it a
   direct lift.

9. For arithmetic variants over a number field \(k\), construct the
   compatible etale Abel--Jacobi class
   \[
     AJ_\ell(Z_\alpha)\in
     H^1(k,H^3_{\mathrm{et}}(X_{\bar k},\Qbb_\ell(2)))
   \]
   and compare it with the de Rham/Deligne realization.

10. Prove any regulator injectivity only on the exact subspace used.
    Without this, motivic vanishing cannot be inferred from
    \(\alpha_X=0\).

11. Recompute the examples. For the quintic, nonzero Yukawa does not
    prove nonzero \(Z_\alpha\) or nonzero \(\alpha_X\). For \(K3\times E\),
    the \(21\)-dimensional \(H^2(\Omega^1)\) target requires a
    class-specific cyclic projection computation.

## Concrete manuscript corrections recommended

The current motivic proposition should not say
\[
  [m_3,B^{(2)}]^{\mathcal M}_X\in H^3_{\mathcal M}(X,\Qbb(2))
\]
as the direct lift of \(\alpha_X\). Replace it by:

```tex
\begin{conjecture}[Motivic normal function for the Atiyah--Connes class]
The Atiyah--Connes class is expected to arise as the infinitesimal
Abel--Jacobi invariant of a homologically trivial codimension-two
motivic class
\[
  Z_\alpha(X)\in H^4_{\mathcal M}(X,\Qbb(2))_{\mathrm{hom}}
  =
  \mathrm{CH}^2(X)_{\mathrm{hom},\Qbb}.
\]
Its Beilinson--Deligne regulator lies in
\[
  J^2(X)_{\Qbb}\subset H^4_{\mathcal D}(X,\Qbb(2)),
\]
and the primitive \(H^{1,2}\)-component of the infinitesimal invariant
of the associated normal function is \(\alpha_X\).
\end{conjecture}
```

Delete or quarantine:

- the torsion graph \([\Gamma_\nabla]\in z^2(X,1)\);
- the claim that \(B^{(2)}\) lifts to \(\mathrm{Pic}(X)_{\Qbb}\);
- the product representative
  \(\Gamma_\nabla\cup c_1(\Omega_X^1)\in \mathrm{CH}^3(X,1)\);
- the unqualified \(\ell\)-adic class in
  \(H^3_{\mathrm{et}}(X,\Qbb_\ell(2))\);
- any statement that regulator injectivity is available in this
  generality.

Keep, but label as frontier:

- a possible secondary \(CH^2(X,1)\) transgression;
- graph-period interpretations of normal-function regulators;
- comparison with Duflo/wheel constants after the cyclic/HKR
  normalisation is fixed;
- Malcev/motivic fundamental group comparisons only after the exact
  configuration-space motive and weight filtration are written.

## Proved / conditional / conjectural split

Proved or primary-source-backed:

- Bloch's higher Chow indexing:
  \(H^i_{\mathcal M}(X,\Qbb(j))=\mathrm{CH}^j(X,2j-i)_{\Qbb}\)
  for the smooth-variety motivic convention used by the manuscript.
- Beilinson--Deligne regulators map motivic cohomology to Deligne or
  absolute Hodge cohomology.
- Codimension-two cycles have Deligne target
  \(H^4_{\mathcal D}(X,\Qbb(2))\), with Abel--Jacobi component
  \(J^2(X)\).
- \(H^{1,2}(X)\) is a quotient/tangent component of \(J^2(X)\), not a
  canonical direct summand of \(H^3_{\mathcal D}(X,\Qbb(2))\).

Conditional:

- The Atiyah--Connes class is a well-defined cyclic/HKR class, pending
  P01's \(B^{(2)}\), total-complex, and projection conventions.
- A Deligne regulator can be compared to \(\alpha_X\), conditional on
  constructing a cycle and computing its infinitesimal invariant.
- \(\ell\)-adic realizations exist in the correct arithmetic
  Abel--Jacobi group, conditional on \(X\) and the cycle descending to a
  number field.

Conjectural:

- Existence of \(Z_\alpha(X)\in \mathrm{CH}^2(X)_{\mathrm{hom},\Qbb}\).
- Equality \(\delta AJ(Z_\alpha)=\alpha_X\).
- Regulator injectivity on the subspace generated by \(Z_\alpha\).
- Motivic vanishing equivalent to Atiyah--Connes vanishing.
- Any \(CH^2(X,1)\) transgression realizing the dual or conjugate
  Atiyah--Connes class.

False as stated:

- A direct lift of \(\alpha_X\) to
  \(H^3_{\mathcal M}(X,\Qbb(2))=\mathrm{CH}^2(X,1)\).
- A canonical higher-Chow representative given by the torsion graph of
  the Chern connection.
- A representative in \(\mathrm{CH}^3(X,1)\) for a class claimed to
  live in \(H^3_{\mathcal M}(X,\Qbb(2))\).
- Unconditional regulator injectivity.

## Next falsifier

The next decisive test is not another status downgrade. It is an
explicit regulator computation in the simplest nontrivial family.

Choose either:

1. a one-parameter quintic degeneration with a known normal function
   from a codimension-two algebraic cycle, then compute whether its
   infinitesimal invariant has the same primitive \(H^{1,2}\) component
   as the Atiyah--Connes projection; or
2. \(Y=S\times E\) with \(S\) a K3 surface, decompose a candidate
   codimension-two cycle under Kunneth, and test whether the Abel--
   Jacobi tangent lands in the two Kunneth summands of
   \(H^2(Y,\Omega_Y^1)\) in the way required by the cyclic projection.

Failure in both examples means the motivic face is only an analogy.
Success in one example gives the paper a genuine motivic theorem to
develop.

## Verification

Commands run locally:

```bash
rg -n -e "motivic" -e "regulator" -e "Deligne" -e "Chow" \
  -e "higher Chow" -e "Beilinson" -e "absolute Hodge" \
  -e "cycle class" -e "Abel" -e "Bloch" -e "\\bCH\\b" \
  -e "alpha_X" -e "Atiyah--Connes" -e "Atiyah-Connes" \
  standalones notes/universal_anomaly_attack_heal_20260424 \
  notes/universal_anomaly_platonic_swarm_20260424 \
  -g '*.tex' -g '*.md'

rg -n -e "H_D\\^4" -e "intermediate Jacobian" \
  -e "Abel--Jacobi" -e "CH\\^2\\(X\\)" -e "CH\\^2\\(X,1\\)" \
  -e "Deligne cohomology" standalones chapters \
  notes/universal_anomaly_platonic_swarm_20260424 \
  -g '*.tex' -g '*.md'
```

No build was run. No target TeX file was edited.
