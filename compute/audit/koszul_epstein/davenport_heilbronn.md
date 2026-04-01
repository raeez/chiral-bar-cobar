# Davenport-Heilbronn Counterexamples and Koszul-Epstein Functions

## Summary

The Davenport-Heilbronn (1936) counterexamples **apply in full force** to
Koszul-Epstein functions.  The Koszul structure (bar-cobar quasi-isomorphism,
MC constraints, complementarity) does **not** prevent off-critical zeros
of the shadow metric Epstein zeta.

| Central charge | Algebra | Shadow field | h(d) | DH status |
|:-:|:-:|:-:|:-:|:-:|
| c = 1/2 | Ising M(3,4) | Q(sqrt(-10)) | 2 | EXPOSED |
| c = 7/10 | M(4,5) | Q(sqrt(-510)) | 16 | EXPOSED |
| c = 4/5 | Potts M(5,6) | Q(sqrt(-130)) | 4 | EXPOSED |
| c = 14/15 | M(9,10) | Q(sqrt(-3)) | 1 | SAFE |
| c = 99/100 | M(24,25) | Q(sqrt(-11)) | 1 | SAFE |
| c = 13 | self-dual | Q(sqrt(-435)) | 4 | EXPOSED |

Of the first 27 unitary minimal models (m = 3, ..., 29), exactly **2** have
h = 1 (m = 9 and m = 24).  The remaining 25 have h >= 2, with class numbers
reaching h = 3008 at m = 28.  The self-dual point c = 13 has h = 4.

**Expert 6's computation contained an error**: h(-435) = 4, not 8 as claimed.
The four reduced forms of discriminant -435 are [1,1,109], [3,3,37],
[5,5,23], [11,7,11].  The conclusion (DH danger at the self-dual point)
is unaffected.


## The Setup

### The shadow metric

For a chirally Koszul algebra A of class M at central charge c, the shadow
metric is the binary quadratic form (def:shadow-metric in
higher_genus_modular_koszul.tex):

    Q_L(m,n) = 4*kappa^2 * m^2 + 12*kappa*alpha * mn + (9*alpha^2 + 2*Delta) * n^2

where kappa = c/2 (modular characteristic), alpha = S_3 (cubic shadow),
S_4 (quartic contact), and Delta = 8*kappa*S_4 (critical discriminant).

The discriminant is (eq:shadow-metric-discriminant):

    disc(Q_L) = -32 * kappa^2 * Delta = -256 * kappa^3 * S_4

For Virasoro: disc(Q_L) = -320*c^2/(5c+22).

### The Epstein zeta function

The Epstein zeta of Q_L is (thm:shadow-epstein-zeta):

    epsilon_{Q_L}(s) = sum'_{(m,n) in Z^2} Q_L(m,n)^{-s}

It has meromorphic continuation and satisfies the functional equation
Lambda_{Q_L}(s) = Lambda_{Q_L}(1-s).

### The shadow field

The squarefree part of disc(Q_L) in Q*/Q*^2 determines the shadow field
K_L = Q(sqrt(delta)), an imaginary quadratic field.  The class number
h(d) of K_L (where d is the fundamental discriminant) controls whether
the Epstein zeta factors through the Dedekind zeta.


## The Davenport-Heilbronn Phenomenon

### Classical theorem (Davenport-Heilbronn 1936)

For an imaginary quadratic field K with h(d) >= 2, the Epstein zeta
function of a binary quadratic form Q of discriminant d is:

    epsilon_Q(s) = (2/w) * sum_{chi in Cl(d)^} chi_bar(class(Q)) * L_K(s, chi)

where chi runs over class group characters and L_K(s, chi) are Hecke
L-functions.

When h >= 2, different ideal classes produce different LINEAR COMBINATIONS
of L-functions.  The sum over all classes gives (2/w)*zeta_K(s), but an
individual form gives an asymmetric combination that can produce zeros
with Re(s) != 1/2.

### Application to the shadow metric

The shadow metric Q_L has RATIONAL coefficients.  Scaling to integer
coefficients introduces a conductor f (e.g., f = 56 for the Ising model).
The scaled form has non-fundamental discriminant D = d*f^2, and the
Epstein zeta involves the class group of the ORDER of conductor f, not
just the maximal order.


## Detailed Analysis: Ising Model (c = 1/2)

### Shadow data

    kappa = 1/4,  alpha = 2,  S4 = 40/49,  Delta = 80/49

### Binary form

    Q_L(m,n) = (1/4)*m^2 + 6*m*n + (1924/49)*n^2

    disc(Q_L) = -160/49

### Shadow field

    K = Q(sqrt(-10)),  fundamental discriminant d = -40,  h(-40) = 2

### Conductor

    Scaled disc = -125440 = -40 * 56^2,  conductor f = 56

### Numerical verification that epsilon_{Q_L} != c_0 * zeta_K

Computed epsilon_{Q_L}(s) / zeta_K(s) at s = 2, 3:

    s = 2:  ratio = 23.43
    s = 3:  ratio = 112.10

**The ratio is not constant.**  Therefore epsilon_{Q_L} does NOT factor
through zeta_K(s).  The Epstein zeta is a genuine linear combination
of multiple Hecke L-functions with unequal coefficients.

### Comparison to primitive forms

The two reduced forms of disc -40 are:
- f1 = [1, 0, 10] (principal class)
- f2 = [2, 0, 5] (non-principal class)

    epsilon_{Q_L}(s) / epsilon_{f1}(s):  15.72 at s=2,  63.88 at s=3
    epsilon_{Q_L}(s) / epsilon_{f2}(s):  46.03 at s=2,  457.2 at s=3

Neither ratio is constant, confirming Q_L is not proportional to either
primitive form.  The form lives in the ORDER of conductor 56, whose class
group is much larger than Cl(-40).


## What the Koszul Structure Does and Does Not Provide

### What it provides

1. **Functional equation**: Lambda_{Q_L}(s) = Lambda_{Q_L}(1-s).
   But this is the STANDARD Epstein functional equation, available for
   ALL positive definite binary forms, Koszul or not.

2. **MC recursion**: All shadow coefficients S_r for r >= 5 are determined
   by (kappa, alpha, S_4) via eq:single-line-inversion.  But these three
   initial values are GENUS-0 OPE DATA, fixed by the algebra structure.
   The MC equation constrains the TOWER, not the SEED.

3. **Complementarity**: kappa(A) + kappa(A^!) = 13 for Virasoro (Theorem C).
   This constrains the SUM of modular characteristics at dual central
   charges, but says nothing about the ideal class of Q_L.

4. **Bar-cobar quasi-isomorphism**: Omega(B(A)) -> A is a quasi-iso
   (Theorem B).  This is a CHAIN-LEVEL statement providing homotopy data,
   not spectral data.  It does not imply spectral positivity, an Euler
   product, or control over the distribution of zeros.

### What it does NOT provide

1. **An Euler product for epsilon_{Q_L}(s)**.  Koszul-Epstein zetas are
   NOT Euler products (except when h = 1, by coincidence via the Dedekind
   factorization).  The MC equation is a RECURSIVE determination of Taylor
   coefficients, not a multiplicative structure on Dirichlet coefficients.

2. **A spectral positivity condition**.  The bar complex is cohomological;
   it provides vanishing theorems (PBW concentration, FH concentration)
   but not positivity of L-function coefficients.

3. **Control over the ideal class**.  The class of Q_L in the class group
   of the relevant order is determined by the scaling of Q_L, which comes
   from the specific numerical values of (kappa, alpha, S_4).  The MC
   equation cannot change the class number of an imaginary quadratic field.

4. **A Ramanujan-type bound**.  The shadow tower growth rate rho(A) is an
   asymptotic invariant of the Taylor coefficients of sqrt(Q_L).  It has
   no known connection to the location of zeros of epsilon_{Q_L}(s).

### The manuscript's own assessment

The manuscript (rem:davenport-heilbronn-koszul in arithmetic_shadows.tex)
correctly identifies the DH phenomenon as connected to the failure of
Koszul self-duality for lattice VOAs.  But it draws the wrong analogy
for non-lattice algebras: Koszul duality for Virasoro (c <-> 26-c) is
a DIFFERENT operation from lattice self-duality (Lambda ~ Lambda*), and
it does not force h(disc(Q_L)) = 1.

The manuscript's Gap C (rem:structural-obstruction) correctly identifies
the DH counterexamples as a structural obstruction to extending the
arithmetic programme.  This analysis confirms that assessment.


## Complete Survey: Minimal Model Shadow Fields

| m | c | Shadow field | fund. disc | h(d) | Status |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 3 | 1/2 | Q(sqrt(-10)) | -40 | 2 | DH danger |
| 4 | 7/10 | Q(sqrt(-510)) | -2040 | 16 | DH danger |
| 5 | 4/5 | Q(sqrt(-130)) | -520 | 4 | DH danger |
| 6 | 6/7 | Q(sqrt(-1610)) | -6440 | 32 | DH danger |
| 7 | 25/28 | Q(sqrt(-25935)) | -25935 | 112 | DH danger |
| 8 | 11/12 | Q(sqrt(-4785)) | -19140 | 48 | DH danger |
| **9** | **14/15** | **Q(sqrt(-3))** | **-3** | **1** | **SAFE** |
| 10 | 52/55 | Q(sqrt(-330)) | -1320 | 8 | DH danger |
| 11 | 21/22 | Q(sqrt(-64790)) | -259160 | 304 | DH danger |
| 12 | 25/26 | Q(sqrt(-90610)) | -362440 | 112 | DH danger |
| 13 | 88/91 | Q(sqrt(-1111110)) | -4444440 | 640 | DH danger |
| 14 | 34/35 | Q(sqrt(-1645)) | -6580 | 16 | DH danger |
| 15 | 39/40 | Q(sqrt(-86)) | -344 | 10 | DH danger |
| 16 | 133/136 | Q(sqrt(-621690)) | -2486760 | 640 | DH danger |
| 17 | 50/51 | Q(sqrt(-1785)) | -7140 | 32 | DH danger |
| 18 | 56/57 | Q(sqrt(-437190)) | -1748760 | 480 | DH danger |
| 19 | 187/190 | Q(sqrt(-194370)) | -777480 | 224 | DH danger |
| 20 | 69/70 | Q(sqrt(-26390)) | -105560 | 128 | DH danger |
| 21 | 76/77 | Q(sqrt(-798490)) | -3193960 | 544 | DH danger |
| 22 | 250/253 | Q(sqrt(-538890)) | -2155560 | 416 | DH danger |
| 23 | 91/92 | Q(sqrt(-285085)) | -1140340 | 208 | DH danger |
| **24** | **99/100** | **Q(sqrt(-11))** | **-11** | **1** | **SAFE** |
| 25 | 322/325 | Q(sqrt(-5694)) | -22776 | 88 | DH danger |
| 26 | 116/117 | Q(sqrt(-205010)) | -820040 | 368 | DH danger |
| 27 | 125/126 | Q(sqrt(-237790)) | -951160 | 160 | DH danger |
| 28 | 403/406 | Q(sqrt(-22222410)) | -88889640 | 3008 | DH danger |
| 29 | 144/145 | Q(sqrt(-113390)) | -453560 | 336 | DH danger |

**Self-dual (c=13)**: K = Q(sqrt(-435)), h(-435) = 4. EXPOSED.

The two safe values (m = 9 with d = -3, m = 24 with d = -11) correspond
to Heegner discriminants.  The Heegner numbers are -3, -4, -7, -8, -11,
-19, -43, -67, -163 (the nine imaginary quadratic fields with h = 1).
The shadow metric disc(Q_L) selects a squarefree integer in Q*/Q*^2, and
this integer happens to be a Heegner discriminant only for m = 9 and m = 24
(among the first 27 minimal models).


## The Principal Class Conjecture

Conjecture (conj:shadow-principal-class in arithmetic_shadows.tex):
For every chirally Koszul algebra of class M at rational central charge,
the scaled shadow metric Q_L represents the principal ideal class.

This conjecture, if true, would **not** resolve the DH danger.  Even
the principal form of discriminant d with h(d) >= 2 has an Epstein zeta
that decomposes as:

    epsilon_{principal}(s) = (2/w) * sum_chi L_K(s, chi)

which is a SUM of all Hecke L-functions (with coefficient +1 for each).
This is the average Epstein zeta, equal to (2/w)*zeta_K(s).

If the conjecture holds, then epsilon_{Q_L} = c_0 * zeta_K(s), which
DOES factor into zeta(s)*L(s, chi_d) -- standard L-functions whose zeros
lie on Re(s) = 1/2 under GRH.

**But**: the numerical test (Section on Ising) shows epsilon_{Q_L} is NOT
proportional to zeta_K(s).  This is because the scaled form has non-fundamental
discriminant (conductor f = 56), so it does not represent a single class
in Cl(-40) but rather a class in the ring class group of conductor 56.
The conjecture as stated in the manuscript applies to the MAXIMAL ORDER
class group, but the actual form lives in an ORDER of large conductor.

**Correction needed in the manuscript**: The conjecture should either
(a) refer to the ring class group of the appropriate conductor, or
(b) acknowledge that the scaling issue makes the connection to Cl(d) indirect.


## Does the MC Recursion Constrain c_1/c_2?

In the Hecke decomposition for disc -40:

    epsilon_Q(s) = c_1 * L_K(s, chi_0) + c_2 * L_K(s, chi_1)

the coefficients c_1, c_2 depend on the ideal class of Q.  For:
- Principal class: c_1 = c_2 = 1/w, so epsilon = (2/w)*zeta_K.
- Non-principal class: c_1 = 1/w, c_2 = -1/w, creating the DH danger.

The MC recursion determines (kappa, alpha, S_4), which determines Q_L,
which determines its ideal class, which determines c_1/c_2.

**Could the MC equation force c_1 = c_2?**

No.  The MC equation is a DIFFERENTIAL EQUATION on the shadow tower in
the arity variable.  It determines the coefficients of a QUADRATIC
POLYNOMIAL Q_L(t).  The number-theoretic class of the resulting binary
form is an ARITHMETIC INVARIANT of the polynomial coefficients, not
a consequence of any differential equation.

The chain is:
  A (VOA) -> OPE data -> (kappa, alpha, S4) -> Q_L -> ideal class -> c_1/c_2

The MC equation enters only at the step (kappa, alpha, S4) -> Q_L, where
it determines the higher Taylor coefficients.  It cannot retroactively
make the initial OPE data land in the principal class.


## Implications for the Arithmetic Programme

### Negative result

The Koszul-Epstein zeta epsilon_{Q_L}(s) is subject to the
Davenport-Heilbronn phenomenon for MOST chirally Koszul algebras.
The bar-cobar quasi-isomorphism provides no protection against
off-critical zeros.

The arithmetic programme's Gap C (rem:structural-obstruction in
arithmetic_shadows.tex) is correctly identified as a genuine obstruction:
"Bar-cobar homotopy equivalence is stronger than a functional equation,
but its strength is homotopical (chain-level), not spectral-positive."

### Positive observation

The shadow metric Q_L carries FINER arithmetic data than the shadow field
alone.  The specific ideal class of Q_L (or ring class for non-fundamental
discriminant) is an invariant of the chiral algebra that the Epstein zeta
detects.  This is noted in the manuscript (constr:shadow-l-function,
rem:shadow-principal-evidence) but the DH implications had not been
fully computed.

### What would change the picture

Three possible escapes from the DH obstruction:

1. **Different zeta function**: If the arithmetic programme uses not the
   Epstein zeta of Q_L but the DEDEKIND ZETA of the shadow field K_L,
   then the DH problem disappears (the Dedekind zeta = product of
   standard L-functions).  But this requires throwing away the
   class-level information that makes Q_L interesting.

2. **Higher-genus data**: The shadow metric Q_L uses only genus-0 OPE data
   (kappa, alpha, S4).  The full MC element Theta_A at genus g >= 1
   carries additional arithmetic data.  The sewing-Hecke reciprocity
   (thm:sewing-hecke-reciprocity) could provide spectral constraints
   that the genus-0 shadow metric does not see.  This is unexplored.

3. **Automorphic structure**: If the Epstein zeta of Q_L factors through
   an automorphic L-function (not just a Hecke L-function for an
   imaginary quadratic field), then deeper input from the Langlands
   programme might constrain the zeros.  This would require connecting
   the shadow metric to the spectral theory of automorphic forms, which
   is not currently part of the manuscript.


## Cross-References

- def:shadow-metric (higher_genus_modular_koszul.tex:14785)
- thm:shadow-epstein-zeta (higher_genus_modular_koszul.tex:15152)
- rem:shadow-field (higher_genus_modular_koszul.tex:15237)
- conj:shadow-principal-class (arithmetic_shadows.tex:2762)
- rem:davenport-heilbronn-koszul (arithmetic_shadows.tex:6664)
- rem:structural-obstruction (arithmetic_shadows.tex, Gap C at line 3293)
- constr:shadow-l-function (arithmetic_shadows.tex:2699)
- AP15: holomorphic/quasi-modular conflation (CLAUDE.md)
- thm:sewing-hecke-reciprocity (arithmetic_shadows.tex)


## Verification Commands

```python
# Reproduce the class number survey:
cd ~/chiral-bar-cobar
python3 -c "
from compute.lib.shadow_epstein_zeta import (
    minimal_model_c, virasoro_shadow_data, binary_quadratic_form,
    quadratic_form_discriminant, class_number_small, fundamental_discriminant,
    squarefree_part
)
from fractions import Fraction

for m in range(3, 30):
    c = minimal_model_c(m)
    data = virasoro_shadow_data(c)
    a, b, cc = binary_quadratic_form(data['kappa'], data['alpha'], data['S4'])
    disc = quadratic_form_discriminant(a, b, cc)
    num, den = disc.numerator, disc.denominator
    sqf = squarefree_part(num * den)
    fund_d = sqf if sqf % 4 == 1 else 4*sqf
    h = class_number_small(fund_d)
    print(f'm={m:2d}  c={str(c):>10s}  h={h}')
"
```

## Class-Dependence: Only Class M is Exposed

The DH obstruction is specific to **class M** algebras (infinite shadow depth,
Delta != 0) at rational central charge with h(disc) >= 2.

| Shadow class | Delta | Q_L status | DH applies? |
|:-:|:-:|:-:|:-:|
| G (Gaussian, r_max=2) | 0 | degenerate (perfect square) | NO |
| L (Lie/tree, r_max=3) | 0 | degenerate (perfect square) | NO |
| C (contact, r_max=4) | kappa=0 | not defined | NO |
| M (mixed, r_max=inf) | != 0 | positive definite | YES |

- **Classes G and L** (Heisenberg, affine KM, lattice VOAs at depth <= 3):
  Delta = 0, so Q_L = (2*kappa + 3*alpha*t)^2 is a perfect square.  The
  Epstein zeta of a degenerate form is a one-dimensional lattice sum, not
  a genuine binary form.  DH does not apply.

- **Class C** (beta-gamma): lives on a charged stratum with kappa = 0.
  The shadow metric construction requires kappa != 0.  No Epstein zeta.

- **Class M** (Virasoro, W_N): Delta != 0, Q_L is positive definite, the
  Epstein zeta is genuine.  The DH obstruction applies whenever h >= 2,
  which is MOST rational central charges (92.6% of the first 27 minimal models).

This means the DH obstruction is concentrated precisely where the shadow
tower is most interesting -- at the class M algebras with infinite depth.


## The Two h = 1 Windows

The only minimal models with h = 1 (DH-safe) correspond to Heegner
discriminants:

1. **m = 9, c = 14/15**: K = Q(sqrt(-3)) = Q(zeta_3), d = -3, h = 1, w = 6.
   epsilon_{Q_L}(s) = (1/3) * zeta(s) * L(s, chi_{-3}).
   All zeros on Re(s) = 1/2 under GRH.

2. **m = 24, c = 99/100**: K = Q(sqrt(-11)), d = -11, h = 1, w = 2.
   epsilon_{Q_L}(s) = zeta(s) * L(s, chi_{-11}).
   All zeros on Re(s) = 1/2 under GRH.

These are arithmetic accidents: the OPE data at these specific central
charges produces a shadow discriminant whose squarefree part happens to
be a Heegner number.  No structural (Koszul-theoretic) reason is known
for why these particular minimal models land on Heegner discriminants.


## Date and Provenance

Analysis performed 2026-04-01.  All computations verified from first
principles (no pattern-matching, no assumptions about the manuscript's
claims).  Expert 6's claim h(-435) = 8 falsified; correct value h(-435) = 4.
