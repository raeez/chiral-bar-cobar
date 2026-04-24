# P16: Heegner / Bruinier / Chenevier arithmetic lane

Owned report:

- `notes/universal_anomaly_platonic_swarm_20260424/P16_heegner_bruinier_chenevier.md`

Target TeX files were read only. No target TeX file was edited.

## Verdict

The arithmetic lane has a true core, but the current nine-discriminant
story is not proved.

The true core is:

\[
  \widetilde H(S,\mathbb Z)=H^{\mathrm{even}}(S,\mathbb Z)
  \quad\text{has signature}\quad (4,20)
\]
for a K3 surface \(S\). Hence
\[
  c_+(\widetilde H(S,\mathbb Z))=4,\qquad
  K_{\mathrm{Muk}}:=2c_+=8
\]
after adopting the Mukai-doubling normalization. This is a lattice
constant. It is not a consequence of Bruinier Proposition 5.1.

The singular-K3 arithmetic core is also true:

\[
  \rho(S)=20
  \quad\Longleftrightarrow\quad
  T(S)\text{ is an oriented positive-definite even rank-2 lattice}.
\]
The discriminant \(d=\det T(S)>0\) is the positive integer attached to
the negative imaginary quadratic discriminant \(-d\). Shioda--Inose
identifies singular K3 surfaces with such oriented lattices, equivalently
with proper binary quadratic forms.

The classical class-number-one fundamental discriminants are exactly
\[
  d\in\{3,4,7,8,11,19,43,67,163\}.
\]

The proposed replacement
\[
  \{3,4,7,8,11,15,19,20,24\}
\]
is not a Bruinier--Chenevier theorem in the present manuscript. It is
exactly the set of fundamental negative discriminants with
\[
  d\le 24,\qquad h(-d)\le 2.
\]
That is an elementary finite initial segment, not a class-number-one
list and not an arithmetic positivity theorem. Keeping it requires a new
explicit coefficient/sign calculation.

## Local anchors read

- Main proposition: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1095`.
- Main K3 arithmetic claims around Bruinier and \(K=8\):
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:370`.
- Local/global supplement, Chenevier and MGSL claims:
  `standalones/universal_anomaly_local_global_arithmetic_supplement.tex:42`.
- VOA supplement, arithmetic VOA construction:
  `standalones/universal_anomaly_voa_explicit_supplement.tex:587`.
- P04 K3/Mukai/Igusa/trace report:
  `notes/universal_anomaly_platonic_swarm_20260424/P04_k3_mukai_igusa_trace.md`.
- Vol III monodromy claims:
  `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:2027`,
  `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:3524`.

## Primary anchors checked

- Bruinier, *Borcherds Products on \(O(2,l)\) and Chern Classes of
  Heegner Divisors*, LNM 1780, Springer, 2002. Public PDF:
  `https://www.mathematik.tu-darmstadt.de/media/algebra/homepages/bruinier/publikationen/c-master.pdf`.
- Chenevier, *The p-adic analytic space of pseudocharacters of a
  profinite group and pseudorepresentations over arbitrary rings*,
  arXiv:0809.0415.
- Chenevier, *On the infinite fern of Galois representations of unitary
  type*, Ann. Sci. ENS 44 (2011), 963--1019.
- Chenevier--Lannes, *Automorphic Forms and Even Unimodular Lattices:
  Kneser Neighbors of Niemeier Lattices*, Springer, 2019.
- Morrison, *On K3 surfaces with large Picard number*, Invent. Math. 75
  (1984), 105--122.
- Kuga--Satake, *Abelian varieties attached to polarized K3 surfaces*,
  Math. Ann. 169 (1967), 239--242.
- Shioda--Inose, *On singular K3 surfaces*, 1977.

## Findings

### CRITICAL 1: Bruinier "Proposition 5.1" is not the claimed theorem

The manuscript repeatedly cites "Bruinier 2002 Proposition 5.1" as a
Heegner--Chern reciprocity theorem forcing:

\[
  K=2c_+=8,\qquad \hbar^2K=-1,\qquad
  \text{rank-8 positivity selecting nine }d_K.
\]

This is false as cited.

In the accessible LNM text, the item labelled 5.1 is a lemma on bases
of vector-valued cusp forms over cyclotomic integer rings. The Chern
class construction is carried by Theorem 5.2 and the later lifting
statements around Theorems 5.8--5.9. The relevant statement sends
Fourier coefficient functionals to Chern classes of Heegner divisors
and constructs a modular generating series of these classes.

What Bruinier supplies:

\[
  a_{\beta,m}\longmapsto \frac12\,c\bigl(H(\beta,-m)\bigr)
\]
and modularity of the Heegner-divisor Chern-class generating series.

What Bruinier does not supply in the cited location:

- no formula \(K=2c_+\);
- no \(\hbar^2K=-1\);
- no order-\(8\) monodromy theorem for \(\Delta_5\);
- no replacement of \(\{43,67,163\}\) by \(\{15,20,24\}\);
- no Chenevier determinant condition.

Repair: cite Bruinier for Heegner-divisor Chern classes and Borcherds
products only. The \(K=8\) value must be stated as Mukai signature plus
the paper's conductor normalization.

### CRITICAL 2: The nine-list is unsupported and misnamed

The manuscript currently separates the classical list and the proposed
rank-\(8\) list, which is the right status direction. The supplement
still treats the proposed list as a structured arithmetic output:

\[
  \{3,4,7,8,11,15,19,20,24\}.
\]

Direct reduced-binary-quadratic-form computation gives:

Class-number-one fundamental negative discriminants:

\[
  \{3,4,7,8,11,19,43,67,163\}.
\]

Class-number-two fundamental negative discriminants:

\[
  \{15,20,24,35,40,51,52,88,91,115,123,148,187,232,235,267,403,427\}.
\]

All order discriminants with class number \(1\):

\[
  \{3,4,7,8,11,12,16,19,27,28,43,67,163\}.
\]

All order discriminants with class number \(2\):

\[
  \{15,20,24,32,35,36,40,48,51,52,60,64,72,75,88,91,99,100,112,115,123,147,148,187,232,235,267,403,427\}.
\]

Thus the proposed nine-list is:

\[
  \{d:\ -d\text{ fundamental},\ h(-d)\le 2,\ d\le 24\}.
\]

That is a true description. It is not the Heegner--Stark--Baker list,
not class number one, and not yet a Bruinier positivity cut.

Repair: either replace the nine-list by the classical class-number-one
list, or define an explicit rank-\(8\) admissibility predicate
\[
  \mathcal C_8(d)
\]
in terms of Fourier coefficients of the exact vector-valued input to
the Borcherds lift, then prove
\[
  \{d:\mathcal C_8(d)\}
  =
  \{3,4,7,8,11,15,19,20,24\}.
\]

### CRITICAL 3: Chenevier determinants do not select the nine discriminants

Chenevier's determinant formalism is a theory of multiplicative
polynomial laws / pseudorepresentations. It is designed to construct and
study pseudodeformation spaces, especially over arbitrary base rings and
in residually reducible situations.

It does not say that unitary \(2\)-dimensional Galois representations
of \(G_{\mathbb Q(\sqrt{-d})}\) are classified by determinants in the
sense needed here. A determinant records characteristic polynomials. It
does not classify representations without semisimplicity and residual
hypotheses, and even then it classifies semisimplifications rather than
the full representation.

Chenevier's infinite fern theorem is a \(U(3)\)-type statement over a
CM field with \(p\) split, about Zariski closures of modular points in
deformation spaces. It does not impose a finite list of imaginary
quadratic discriminants. It also does not interact with Bruinier
Heegner coefficients without an extra automorphic/Galois comparison
map.

Repair: Chenevier may enter only after the paper defines:

1. a residual representation \(\bar\rho_d\);
2. a pseudodeformation determinant \(D_d\);
3. a map from the Bruinier Heegner coefficient datum to the determinant
   deformation ring;
4. a theorem that the determinant condition is equivalent to
   \(\mathcal C_8(d)\).

Until those four objects exist, "Bruinier--Chenevier refinement" is a
name for an open problem, not a theorem.

### CRITICAL 4: The arithmetic VOA construction is not defined

The VOA supplement writes

\[
  V^{\mathrm{arith}}_{K3,d}
  =
  \bigl(V_{\mathrm{Muk}(K3)}\bigr)^{\sigma_d}
  \otimes \mathbb C[\mathcal O_d/\mathcal O_d^*].
\]

This is not a valid class-group construction.

The quotient \(\mathcal O_d/\mathcal O_d^*\) is not the ideal class
group. The correct arithmetic finite group is the proper ideal class
group

\[
  \mathrm{Pic}(\mathcal O_d)
  =
  I(\mathcal O_d)/P^+(\mathcal O_d)
\]

or the form class group of primitive positive-definite binary quadratic
forms of discriminant \(-d\). The additive quotient by units is infinite
and does not produce a finite class-group algebra.

Nor does a Hilbert-class-field automorphism
\(\sigma_d\in\mathrm{Gal}(H_d/\mathbb Q)\) act canonically on the
complex lattice VOA \(V_{\mathrm{Muk}(K3)}\) without specifying an
integral model, CM field of definition, Galois descent datum, and
compatibility with the lattice cocycle.

Repair: replace the arithmetic VOA theorem by a conjectural construction:

\[
  V^{\mathrm{arith}}_{K3,d}
  \quad\text{exists if a CM descent datum on }V_{\mathrm{Muk}(K3)}
  \text{ and a }\mathrm{Pic}(\mathcal O_d)\text{-action are constructed.}
\]

The class-group algebra, if used, is
\[
  \mathbb C[\mathrm{Pic}(\mathcal O_d)],
\]
not \(\mathbb C[\mathcal O_d/\mathcal O_d^*]\).

### SERIOUS 1: The displayed transcendental lattices are not correct

For a singular K3, the transcendental lattice is an even positive
rank-\(2\) lattice with Gram matrix

\[
  T =
  \begin{pmatrix}
  2a & b\\
  b & 2c
  \end{pmatrix},
  \qquad
  \det T = 4ac-b^2=d.
\]

It corresponds to the binary quadratic form \([a,b,c]\) of discriminant
\(-d=b^2-4ac\).

The supplement's odd-discriminant diagonal formula

\[
  \mathrm{diag}\bigl(2,(1+d)/2\bigr)
\]

has determinant \(d+1\), not \(d\). For \(d=3\) it gives determinant
\(4\); for \(d=7\) it gives determinant \(8\). It cannot represent the
transcendental lattice of discriminant \(d\).

Repair: never give a single diagonal \(T_d\) unless the exact binary
quadratic form class has been chosen. The canonical statement is in
terms of classes \([a,b,c]\), not a universal diagonal matrix.

### SERIOUS 2: \(d=8,20,24\) are not non-maximal conductor-\(2\) orders

The supplement says that \(d=8,20,24\) are non-maximal conductor-\(2\)
orders over \(d=4,5,6\). This is false for the usual discriminant
convention.

\[
  -8,\ -20,\ -24
\]

are fundamental discriminants, attached respectively to

\[
  \mathbb Q(\sqrt{-2}),\quad
  \mathbb Q(\sqrt{-5}),\quad
  \mathbb Q(\sqrt{-6}).
\]

Examples of non-maximal order discriminants in this range are instead
\[
  -12,\ -16,\ -27,\ -28.
\]

Repair: state \(d=8,20,24\) as maximal/fundamental discriminants.

### SERIOUS 3: The unit-group rationale is false

Every imaginary quadratic order has units \(\{\pm 1\}\). Extra units
occur only for

\[
  D=-3 \quad(\mu_6),\qquad D=-4 \quad(\mu_4).
\]

The unit group cannot select the nine-list, the class-number-one list,
or the proposed rank-\(8\) list.

Repair: remove every unit-group explanation of the discriminant
selection. Units may enter only as stabilizer factors in class number
formulae, not as an admissibility criterion.

### SERIOUS 4: Kuga--Satake and MGSL are over-attributed

The Kuga--Satake construction attaches a high-dimensional abelian
variety to a polarized K3 Hodge structure. For K3 surfaces the relevant
dimension is convention-dependent but is of Clifford size; it is not a
map to \(\mathcal A_2\) in general.

Humbert divisors \(H_D\subset\mathcal A_2\) are divisors for principally
polarized abelian surfaces. Their direct use after a Kuga--Satake lift
to \(\mathcal A_g\) requires an additional special subvariety or
projection. This extra map is not constructed in the paper.

The "Mumford--Tate--Galois--Sato--Lannes conjecture" is not a standard
named theorem of Chenevier--Lannes 2019. Chenevier--Lannes concerns
automorphic forms and even unimodular lattices via Kneser neighbors and
Niemeier lattices. It does not prove a motivic Galois factorization for
K3-fibered Calabi--Yau threefolds, nor a theorem for \(K3\times E\).

Repair: replace MGSL by an explicitly named internal conjecture:

\[
  \mathrm{MT/KS\ admissibility\ conjecture}.
\]

State it as conjectural unless a precise theorem of Deligne, Andre,
Rizov, Madapusi Pera, or another Kuga--Satake source is imported with
its hypotheses.

### MODERATE: Morrison citation drift

The standalone bibliography contains Morrison, *The Kuga--Satake
variety of an abelian surface*, J. Algebra 92 (1985), while the
supplement cites Morrison 1984 Theorem 7.9 and Theorem 8.1. These are
not the same citation surface.

Morrison 1984, *On K3 surfaces with large Picard number*, is a source
for large-Picard K3 / Shioda--Inose arithmetic. It is not a theorem
that the motivic Galois group of \(K3\times E\) factors through the
Mukai orthogonal group in the form used here.

Repair: split the citations:

- Shioda--Inose / singular K3: Shioda--Inose 1977; Morrison 1984.
- Kuga--Satake construction: Kuga--Satake 1967; Deligne 1972; modern
  integral refinements if needed.
- Motivic Galois / Mumford--Tate: Andre / Deligne / modern K3
  Kuga--Satake literature, with explicit theorem numbers.

## Exact lists and constants

### Lattice and automorphic constants

\[
  \operatorname{sig}\widetilde H(K3,\mathbb Z)=(4,20).
\]

\[
  c_+=4,\qquad K_{\mathrm{Muk}}=2c_+=8.
\]

\[
  \Delta_5\text{ has weight }5,\qquad
  \Phi_{10}=\Delta_5^2.
\]

\[
  \hbar^2=-1/8
\]

is conditional on the conductor normalization
\[
  \hbar^2K_{\mathrm{Muk}}=-1.
\]
It is not a Todd trace computation and not a direct Bruinier theorem.

### Discriminants

Fundamental class-number-one:

\[
  \mathcal H_1^{\mathrm{fund}}
  =
  \{3,4,7,8,11,19,43,67,163\}.
\]

Fundamental class-number-two:

\[
  \mathcal H_2^{\mathrm{fund}}
  =
  \{15,20,24,35,40,51,52,88,91,115,123,148,187,232,235,267,403,427\}.
\]

All order discriminants with class number one:

\[
  \mathcal H_1^{\mathrm{ord}}
  =
  \{3,4,7,8,11,12,16,19,27,28,43,67,163\}.
\]

All order discriminants with class number two:

\[
  \mathcal H_2^{\mathrm{ord}}
  =
  \{15,20,24,32,35,36,40,48,51,52,60,64,72,75,88,91,99,100,112,115,123,147,148,187,232,235,267,403,427\}.
\]

Proposed manuscript list:

\[
  \mathcal N_9
  =
  \{3,4,7,8,11,15,19,20,24\}
  =
  \{d\le24:\ -d\text{ fundamental},\ h(-d)\le2\}.
\]

That equality is proved by direct reduced-form enumeration. It is not
the desired rank-\(8\) arithmetic theorem.

## Corrected theorem / conjecture split

### Theorem A: singular K3 discriminant surface

For a complex singular K3 surface \(S\), the oriented transcendental
lattice \(T(S)\) is an even positive-definite rank-\(2\) lattice. Writing

\[
  T(S)=
  \begin{pmatrix}
  2a & b\\ b & 2c
  \end{pmatrix}
\]

gives discriminant

\[
  d=\det T(S)=4ac-b^2.
\]

Shioda--Inose identifies singular K3 surfaces with oriented classes of
such lattices, equivalently with proper classes of positive binary
quadratic forms of discriminant \(-d\). The class-number-one
fundamental discriminants are exactly

\[
  \{3,4,7,8,11,19,43,67,163\}.
\]

Status: proved elsewhere.

### Theorem B: Mukai conductor constant

For every K3 surface,

\[
  \widetilde H(S,\mathbb Z)
  =
  H^0(S,\mathbb Z)\oplus H^2(S,\mathbb Z)\oplus H^4(S,\mathbb Z)
\]

with the Mukai pairing has signature \((4,20)\). Under the
Mukai-doubling convention of this paper,

\[
  K_{\mathrm{Muk}}=2c_+=8.
\]

Status: lattice-theoretic core proved; the identification of this
constant with a derived-centre trace is conditional on the trace
normalization.

### Theorem C: Bruinier input

Bruinier's Borcherds-product theory gives automorphic forms on
orthogonal Shimura varieties whose divisors are Heegner divisors with
multiplicities read from principal-part Fourier coefficients, and gives
modularity of the generating series of Chern classes of Heegner
divisors.

Status: proved elsewhere. It does not imply \(K=8\), \(\hbar^2=-1/8\),
or the proposed nine-list without additional calculations.

### Conjecture D: rank-\(8\) admissible discriminants

Define an explicit predicate \(\mathcal C_8(d)\) by:

1. choose the exact vector-valued modular input \(f_8\) to the
   Borcherds lift;
2. define the Heegner coefficient/sign condition at discriminant
   \(-d\);
3. impose the Mukai conductor normalization \(K_{\mathrm{Muk}}=8\);
4. if Chenevier is used, define a residual determinant datum whose
   pseudodeformation condition is equivalent to the Heegner condition.

The conjecture is:

\[
  \{d:\mathcal C_8(d)\}
  =
  \{3,4,7,8,11,15,19,20,24\}.
\]

Status: conjectural/open. No current source proves it.

### Conjecture E: arithmetic K3 VOA

For \(d\) satisfying the verified admissibility predicate, there exists
a CM descent datum on the Mukai lattice VOA and a finite class-group
action

\[
  \mathrm{Pic}(\mathcal O_{-d})\curvearrowright V_{\mathrm{Muk}(K3)}
\]

such that the arithmetic specialization

\[
  V^{\mathrm{arith}}_{K3,d}
\]

has Mukai conductor \(K_{\mathrm{Muk}}=8\) and the correct
\(\Delta_5\)-Borcherds denominator shadow.

Status: conjectural. The current formula with
\(\mathcal O_d/\mathcal O_d^*\) should be removed.

## Remove / downgrade list

Remove from theorem surfaces:

- "Bruinier 2002 Proposition 5.1 forces \(K=2c_+=8\)."
- "Bruinier positivity cut selects
  \(\{3,4,7,8,11,15,19,20,24\}\)."
- "Chenevier determinants classify the required unitary Galois
  representations."
- "The class group is \(\mathcal O_d/\mathcal O_d^*\)."
- "\(d=8,20,24\) are non-maximal conductor-\(2\) orders."
- "MGSL is in the nomenclature of Chenevier--Lannes 2019."
- "Morrison 1984 proves the \(K3\times E\) motivic Galois statement."
- "Each of the nine discriminants carries a canonical arithmetic VOA."

Keep as proved:

- Mukai signature \((4,20)\).
- \(c_+=4\).
- \(K_{\mathrm{Muk}}=8\) after the paper's doubling convention.
- \(\Delta_5\) weight \(5\), \(\Phi_{10}=\Delta_5^2\).
- Singular K3 / positive binary quadratic form correspondence.
- Classical class-number-one list.

Keep as conditional:

- \(\hbar^2=-1/8\) as the normalized derived-centre conductor.
- The rank-\(8\) nine-list.
- The Kuga--Satake/Humbert intersection with the Atiyah admissible
  locus.
- Chenevier determinant participation.

Keep as conjectural:

- Arithmetic VOAs \(V^{\mathrm{arith}}_{K3,d}\).
- MGSL-type motivic Galois refinement.
- Any Niemeier / \(M_{23}\) arithmetic refinement not directly reduced
  to Chenevier--Lannes plus a constructed chiral bialgebra.

## Next proof step

The decisive computation is not another status downgrade. It is the
construction of the predicate \(\mathcal C_8(d)\). The smallest useful
calculation is:

1. Write the exact weakly holomorphic vector-valued modular form
   \(f_8=\sum c(\beta,m)e_\beta q^m\) whose Borcherds product is the
   \(\Delta_5\)-normalised K3 arithmetic form.
2. For each fundamental \(d\) with \(h(-d)\le2\), compute the relevant
   coefficient/sign entering the Heegner divisor \(H(\beta,d)\).
3. Check whether the set selected is actually
   \(\{3,4,7,8,11,15,19,20,24\}\), the classical
   class-number-one list, or a different finite set.

Until that computation is in the tree, the arithmetic lane should be
marketed as a conjectural rank-\(8\) Heegner filter attached to the
proved Mukai conductor \(K_{\mathrm{Muk}}=8\), not as a theorem.

