# Deligne Categories, Complex Rank, and the Real-to-Complex Spectral Bridge

## Investigation Summary

**Question**: Can Deligne-category techniques extend the shadow obstruction tower / Epstein zeta /
constrained Epstein to complex spectral parameters in a way that sees the zeta zeros?

**Short answer**: No. Deligne categories provide an elegant categorical interpolation
of representation-theoretic *structures* to complex rank, and Zeng's recent work
constructs VOAs inside these categories. But the specific obstruction identified
in the arithmetic shadows programme (rem:structural-obstruction,
thm:structural-separation) is not a rank-interpolation problem — it is a
spectral-vs-algebraic problem. The Deligne category framework does not resolve
it, for precise structural reasons analyzed below.

---

## 1. What Deligne Categories Are (Rigorously)

### 1.1 The Construction

Deligne (2007) constructed rigid symmetric monoidal categories Rep(S_t), Rep(GL_t),
Rep(O_t), Rep(Sp_{2t}) for t in C, interpolating the tensor categories of
finite-dimensional representations of the corresponding groups at integer rank.

**Key properties (PROVED in the literature)**:
- Rep(GL_t) is a C-linear Karoubian rigid symmetric monoidal category.
- For t = n in Z_{>=0}, there is a tensor functor Rep(GL_t) --> Rep(GL_n(C))
  whose kernel consists of "negligible morphisms."
- Rep(GL_t) is NOT abelian for generic t in C \ Z_{>=0}. It is only
  Karoubian (=pseudo-abelian = idempotent-complete). The abelian envelope
  was constructed by Entova-Aizenbud--Serganova (2020) as the category V_t.
- Objects in Rep(GL_t) are formal direct summands of tensor products of the
  "standard object" V_t and its dual V_t*. There is no underlying vector space
  of dimension t — the dimension is a *formal parameter*.
- Morphism spaces ARE finite-dimensional vector spaces over C, described via
  generators and relations (walled Brauer algebra for GL_t, Brauer algebra
  for O_t/Sp_{2t}, partition algebra for S_t).

**Key references**:
- Deligne, "La catégorie des représentations du groupe symétrique S_t,
  lorsque t n'est pas un entier naturel" (2007)
- Etingof, "Representation theory in complex rank, I" (arXiv:1401.6321, 2014)
- Etingof, "Representation theory in complex rank, II" (arXiv:1407.0373, 2016)
- Entova-Aizenbud--Serganova, "Deligne categories and the limit of
  categories Rep(GL(m|n))" (arXiv:1511.07699, 2020)

### 1.2 Complex-Rank Analogues of Standard Objects

Etingof (2014, 2016) defined and studied complex-rank analogues of:

1. **Parabolic category O**: O_t(gl_t) for t in C. Objects are modules
   in the Deligne category Rep(GL_t) with a compatible action of gl_t
   (itself an ind-algebra in Rep(GL_t)).

2. **Yangians**: Y(gl_t) as an associative ind-algebra in Rep(GL_t).
   Kalinov (2020, arXiv:1906.07905) classified simple finite-length
   modules over Y(gl_t) using ultraproduct techniques. This was extended
   to twisted Yangians Y(o_t), Y(sp_t) by Kannan-Kanungo (arXiv:2505.06463).

3. **Affine Lie algebras**: The current algebra g_t-hat can be defined as
   an ind-algebra in Rep(GL_t). Etingof discussed Kac-Moody-type vertex
   algebras in Deligne categories.

**Critical caveat (PROVED)**: These "complex-rank" objects live INSIDE the
Deligne category. Their morphism spaces, character formulas, and structural
constants are polynomials or rational functions of t, obtained by interpolation
from integer values. The category itself has NO extra analytic structure in t
beyond algebraicity — there is no "analytic continuation" in the categorical
sense, only polynomial interpolation.

---

## 2. Zeng's Construction: VOAs in Deligne Categories

### 2.1 What Zeng Constructs (arXiv:2503.03004, November 2025)

Keyou Zeng defines the notion of a vertex algebra object in a symmetric
monoidal category C and constructs specific examples:

- **Beta-gamma VOA in Rep(GL_t)**: The beta-gamma system has N copies of
  (beta, gamma) fields, with symmetry group GL_N. By replacing Rep(GL_N)
  with Rep(GL_t), one obtains a "beta-gamma VOA in the Deligne category"
  for any t in C. The OPE coefficients are polynomial in t.

- **Large-N vertex algebra**: The construction provides a rigorous
  framework for the "large-N vertex algebra" appearing in physics, which
  previously lacked mathematical definition.

- **Vertex Poisson algebra limit**: Zeng also analyzes the classical limit,
  obtaining a vertex Poisson algebra in the Deligne category.

### 2.2 What Zeng Does NOT Construct

- No affine Kac-Moody VOA V_k(gl_t) for arbitrary t in C and k in C
  simultaneously. The level k is a separate parameter from the rank t.
  At integer t = N, V_k(gl_N) is the standard affine KM algebra. The
  Deligne category interpolates the N, not the k.

- No W-algebras W_k(gl_t, f) in the Deligne category (this would require
  defining quantum DS reduction inside a symmetric monoidal category).

- No modular/genus-1 theory: partition functions, characters, and modular
  properties are NOT part of the Deligne category framework. The category
  is a genus-0 (algebraic/operadic) structure. Genus-1 data (traces over
  modules, characters, partition functions) requires MODULES of the VOA,
  and the module theory in Deligne categories is at an early stage.

---

## 3. The Kazhdan-Lusztig Equivalence at Complex Rank

### 3.1 What Is Known

The KL equivalence at integer level k and integer rank N states:

  O_k^int(gl_N-hat) ≃ C(U_q(gl_N)),   q = exp(pi*i/(k + N))

as braided tensor categories (Kazhdan-Lusztig 1993).

**At complex rank t**: One can define O_k(gl_t-hat) as a category internal
to Rep(GL_t), and U_q(gl_t) as an algebra in Rep(GL_t) (via Etingof's
construction). The question is whether

  O_k^int(gl_t-hat) ≃ C(U_q(gl_t))   for t in C

**Status**: This is OPEN. The difficulty is that the KL proof uses
geometric methods (conformal blocks, fusion, braiding) that do not
directly generalize to the Deligne category setting. Kalinov's
ultraproduct technique classifies simple modules of Y(gl_t) but does
not establish the braided equivalence.

### 3.2 Connection to Bar-Cobar Duality

The monograph's Theorem (thm:km-quantum-groups) proves that chiral Koszul
duality induces q <--> q^{-1} at the quantum group level for integer rank.
At complex rank:

- The Koszul dual (gl_t-hat_k)^! = gl_t-hat_{-k-2t} (where h^v = t for gl_t)
  would send q = exp(pi*i/(k+t)) to q^{-1} = exp(-pi*i/(k+t)).
- This is well-defined as a formal statement for any t in C.
- But the *proof* of thm:km-quantum-groups uses the KL equivalence at
  integer rank, which is not available at complex rank.

**Assessment**: The Koszul duality k <--> -k-2h^v is a purely algebraic
operation on the level that extends trivially to complex rank (it is linear
in k and t). But the KL equivalence that gives it categorical meaning is
not proved at complex rank. The bar-cobar framework operates at the level
of the chiral algebra itself, not its module category, so the
extension to complex rank via Deligne categories is structurally possible
for the algebra but not yet for the categorical equivalence.

---

## 4. The Shadow Tower at Complex Central Charge

### 4.1 What Already Extends to Complex c

The shadow obstruction tower is ALREADY defined at complex central charge c in C. All
formulas are polynomial/rational in c:

- kappa(Vir_c) = c/2  (linear in c)
- S_3(Vir_c) = -2  (constant)
- S_4(Vir_c) = 10/[c(5c+22)]  (rational in c)
- Q_L(m,n; c) = c^2 m^2 + 12c*mn + [36 + 80/(5c+22)]*n^2  (rational in c)
- Shadow generating function H(t,c) = t^2 * sqrt(Q_L(t,c))  (algebraic)
- Critical discriminant Delta(c) = 8*(c/2)*10/[c(5c+22)] = 40/(5c+22)
  (rational in c)
- Shadow radius rho(c) = sqrt(9*alpha^2 + 2*Delta) / (2|kappa|)  (algebraic)

None of these formulas use the fact that c is real. They are rational
functions of c, hence holomorphic on C minus a finite set of poles
(c = 0, c = -22/5). The shadow obstruction tower "at complex c" is simply the
evaluation of these rational functions at c in C.

**This is NOT an insight from Deligne categories.** The shadow obstruction tower's
extension to complex c is a trivial consequence of its algebraic definition.
Deligne categories are not needed for this extension, and they add nothing
to it.

### 4.2 The Koszul-Epstein Function at Complex c

The Koszul-Epstein function epsilon^KE_{Vir_c}(s) = Sum'_{(m,n)} Q_L(m,n;c)^{-s}
raises a different question at complex c:

**Problem**: For real c > 0, Q_L(m,n;c) is a positive-definite binary
quadratic form (when Delta > 0), and the Epstein zeta function converges for
Re(s) > 1 and admits meromorphic continuation to all s in C.

For complex c: Q_L(m,n;c) is a complex-valued quadratic form on Z^2.
The Epstein zeta function of a complex quadratic form Sum' Q(m,n)^{-s} is
NOT standard — Q(m,n) is a complex number, so Q(m,n)^{-s} = exp(-s*log Q(m,n))
requires a branch cut choice. The sum may not converge.

**Rigorous assessment**: The Koszul-Epstein function epsilon^KE(s,c) admits
analytic continuation in BOTH s and c, but through different mechanisms:
- In s: via theta-function representation / Mellin-Barnes integral
  (Chowla-Selberg method), working for any c with Q_L positive-definite.
- In c: the coefficients Q_L(m,n;c) are rational in c, so for each
  fixed (m,n), Q_L(m,n;c)^{-s} is analytic in c (away from zeros of Q_L).
  But the SUM over (m,n) introduces convergence issues.

The double analytic continuation (simultaneously in s and c) would require
the theory of families of Epstein zeta functions parametrized by a complex
variable. This is a well-studied topic in the theory of binary quadratic
forms:
- Epstein (1903): analytic continuation in s for fixed real positive-definite Q.
- Terras (1976): families of Epstein zeta functions over complex quadratic forms.
- The Davenport-Heilbronn phenomenon: Epstein zeta functions of indefinite
  quadratic forms can have zeros OFF the critical line.

**The Davenport-Heilbronn obstruction**: For REAL indefinite quadratic forms,
Davenport-Heilbronn (1936) proved that the Epstein zeta function has zeros
off the critical line Re(s) = 1/2. The shadow metric Q_L at complex c is
a COMPLEX quadratic form, which is the analytic continuation of a positive-
definite form. Its Epstein zeta function (once defined) would inherit the
functional equation from the real case by analytic continuation, but would
NOT be expected to satisfy GRH — its zeros are unconstrained.

### 4.3 Why Complex c Does Not See the Zeta Zeros

The structural obstruction (thm:structural-separation) operates at a
different level than the c-parameter:

**The obstruction**: The MC element Theta_A determines the scattering
coupling E_rho(A) = I((1+rho)/2; A) for each nontrivial zero rho of zeta.
The value E_rho is a well-defined holomorphic function of the evaluation
point s = (1+rho)/2. But the LOCATION of rho is a property of zeta(s),
which is independent of the chiral algebra A. No matter what value c takes
(real or complex), the Koszul-Epstein function epsilon^c_s(A) evaluated at
s = (1+rho)/2 gives a coupling constant, not a zero-location constraint.

**Precise statement**: Varying c in C gives a family of Koszul-Epstein
functions {epsilon^KE(s, c)}_{c in C}. Each member is a Dirichlet series
in s with coefficients that depend rationally on c. The zeros of
epsilon^KE(s, c) in the s-variable move as c varies — but these are
zeros of the Koszul-Epstein function, NOT zeros of the Riemann zeta function.
The zeta zeros appear as evaluation points for the scattering coupling,
not as zeros of the Koszul-Epstein function.

**The c-continuation gives no leverage because**:
1. The scattering matrix phi(s) = Lambda(1-s)/Lambda(s) is INDEPENDENT of c.
   It is a property of the Eisenstein series E_s on the modular curve, not
   of the chiral algebra.
2. The RS integral I(s; A) is holomorphic at the scattering poles s = rho/2
   (prop:scattering-residue). This holomorphy is a THEOREM, not a deficiency.
   It holds for ALL c, real or complex.
3. The Kahler potential's arithmetic part log|eta|^2 is pluriharmonic
   (prop:arith-geom-decomposition), hence invisible to Kahler geometry.
   This is a property of eta, not of c.

None of these three structural facts is affected by continuing c to C.

---

## 5. The Deligne Category Bridge: What It Actually Provides

### 5.1 The Rank Parameter vs the Spectral Parameter

The fundamental confusion in the proposed bridge is between two different
kinds of "complex parameter":

- **Rank parameter t in Rep(GL_t)**: interpolates the dimension of the
  fundamental representation. This is an ALGEBRAIC parameter — all
  invariants are polynomial/rational in t.

- **Spectral parameter s in the Eisenstein series**: a complex variable in
  which the scattering matrix phi(s) has poles at zeta zeros. This is an
  ANALYTIC parameter — its behavior is controlled by the distribution of
  primes, not by algebraic identities.

Deligne categories interpolate in the RANK direction. The zeta zeros live
in the SPECTRAL direction. These are orthogonal.

### 5.2 The Virasoro Central Charge as a Rank Parameter

The observation that "the Virasoro central charge c is already a continuous
parameter" is correct but misleading. The central charge c parametrizes a
FAMILY of chiral algebras {Vir_c}_{c in C}. For each c, the algebra Vir_c
has its own shadow obstruction tower, its own Koszul-Epstein function, its own partition
function on M_{1,1}. The shadow obstruction tower coefficients S_r(c) are rational
functions of c.

This is NOT the same as interpolating to "complex rank" in the Deligne sense.
The Virasoro algebra has no GL_N symmetry to interpolate. The W_N algebras
DO have such a structure (DS reduction from gl_N), and the W_{infinity}
limit is the large-N limit. Zeng's construction could in principle define
W_t algebras in Rep(GL_t) for t in C. But this interpolates the NUMBER OF
GENERATORS, not the spectral parameter.

Concretely: W_N has generators of spins 2, 3, ..., N. The shadow obstruction tower of
W_N depends on c AND N. Interpolating N to complex values (via Deligne
categories) gives a "W_t shadow obstruction tower" that is polynomial in t. This is
related to the W_{infinity} limit (N --> infinity), not to the zeta zeros.

### 5.3 What a Complex-Rank KL Equivalence Would Give

If the KL equivalence were proved at complex rank:

  O_k^int(gl_t-hat) ≃ C(U_q(gl_t)),   q = exp(pi*i/(k+t))

then Koszul duality would give:

  O_{-k-2t}^int(gl_t-hat) ≃ C(U_{q^{-1}}(gl_t))

This is a categorical statement about modules, not about zeta zeros. The
quantum group parameter q = exp(pi*i/(k+t)) depends on the level k and
rank t, not on the spectral parameter s. Varying q traces out a circle
in C* (as k varies) or a spiral (as t varies), not the critical line
Re(s) = 1/2.

---

## 6. Honest Assessment: What Deligne Categories Could Contribute

### 6.1 Genuine Mathematical Contributions (PLAUSIBLE)

1. **Uniform proofs across rank**: If a property of the shadow obstruction tower
   (e.g., kappa-additivity, shadow depth classification) holds for all
   W_N uniformly in N, then a proof inside Rep(GL_t) would establish it
   for all t simultaneously. This is a PROOF TECHNIQUE, not a bridge to
   zeta zeros.

2. **W_{infinity} shadow obstruction tower**: The large-N limit of the W_N shadow
   tower is controlled by kappa(W_N) = c*(H_N - 1), where H_N is the
   N-th harmonic number. The Deligne-category version would give
   kappa(W_t) = c*(H_t - 1) where H_t = psi(t+1) + gamma is the
   digamma function (the analytic continuation of H_N). This is a
   meromorphic function of t with poles at t = -1, -2, -3, ... .
   The poles of H_t are at NEGATIVE INTEGERS, not at zeta zeros.

3. **Uniform formality/Koszulness**: If chiral Koszulness for W_N can
   be proved inside Rep(GL_t), it would establish Koszulness of W_t
   for all complex t, hence of W_{infinity} as a formal limit.

4. **DS reduction at complex rank**: Quantum Drinfeld-Sokolov reduction
   inside the Deligne category would give a functorial construction of
   W_t from gl_t-hat. This is mathematically interesting but concerns
   the ALGEBRAIC structure, not the ARITHMETIC interface.

### 6.2 What Deligne Categories Cannot Do (STRUCTURAL IMPOSSIBILITY)

1. **Bridge the spectral gap**: The zeta zeros at s = rho are properties
   of the Eisenstein series on M_{1,1}, independent of any chiral algebra
   or its rank. Varying the rank t does not introduce new spectral data.

2. **Overcome unfolding erasure**: The RS integral I(s; A) is holomorphic
   at scattering poles for ALL A, regardless of rank. This is a theorem
   about the Rankin-Selberg method, not about representation categories.

3. **Access the arithmetic part of the Kahler potential**: log|eta|^2 is
   pluriharmonic for any chiral algebra. Changing the underlying
   representation category does not affect the Kahler geometry of M_{1,1}.

4. **Provide genuinely new analytic continuation**: The Koszul-Epstein
   function epsilon^KE(s,c) already extends to complex c by rationality
   of its coefficients. The Deligne category adds no new analytic data
   beyond what polynomial interpolation already provides.

---

## 7. Where the Real Bridge Might Lie

The arithmetic shadows chapter (sec:complexified-modular-integral) already
identifies two genuine candidate approaches:

### 7.1 Higher Genus (the Programme's Own Candidate)

At genus g >= 2, the Liouville action is nonlinear (R_{g_0} != 0), and
complex saddle points of the genus-g path integral might retain scattering
data that the genus-1 Rankin-Selberg method erases. This is
conj:complex-saddle-scattering.

### 7.2 Spectral Determinant Side

The spectral zeta function zeta_Delta(s) of the Laplacian on E_tau admits
meromorphic continuation via the Epstein functional equation. Its structure
at scattering poles s = rho/2 is not subject to unfolding erasure. But it
encodes the GEOMETRY of E_tau, not the ALGEBRA of A.

### 7.3 What Would Actually Work (Speculative)

The only known route from algebraic/categorical structures to zeta zeros is
the Langlands programme itself:

- Automorphy of L-functions attached to VOA modules (via converse theorems)
- Langlands functoriality applied to the KL equivalence
  (VOA modules <--> quantum group reps --> automorphic forms)
- The geometric Langlands equivalence at critical level (bar complex = opers)
  extended to generic level

None of these involve Deligne categories as an essential ingredient. They
involve the Langlands programme, which is a separate mathematical universe.

---

## 8. Literature Inventory

### 8.1 Papers on Deligne Categories and VOAs

| Reference | Content | Relevance |
|-----------|---------|-----------|
| Zeng, arXiv:2503.03004 (2025) | beta-gamma VOA in Rep(GL_t); large-N VA | Direct: first VOA-in-Deligne construction |
| Etingof, arXiv:1401.6321 (2014) | Rep theory in complex rank I: parabolic O | Framework: category O at complex rank |
| Etingof, arXiv:1407.0373 (2016) | Rep theory in complex rank II: Yangians, affine | Framework: Yangians, affine algebras at complex rank |
| Kalinov, arXiv:1906.07905 (2020) | Finite-dim reps of Y(gl_t) via ultraproducts | Classification: simple Y(gl_t)-modules |
| Kannan-Kanungo, arXiv:2505.06463 (2025) | Twisted Yangians at complex rank | Extension: Y(o_t), Y(sp_t) |
| Entova-Aizenbud-Serganova (2020) | Abelian envelope of Rep(GL_t) | Structure: the correct abelian framework |
| Deligne (2007) | Original construction of Rep(S_t) | Foundation |

### 8.2 Papers Already in the Monograph's Bibliography

| BibKey | Connection |
|--------|------------|
| GLZ / Gui-Li-Zeng, arXiv:2212.11252 | Quadratic duality for chiral algebras (Zeng is a coauthor) |
| KL93 / Kazhdan-Lusztig | KL equivalence (used in thm:km-quantum-groups) |

### 8.3 Papers NOT in the Bibliography That Should Be Noted

| Reference | Why |
|-----------|-----|
| Zeng 2503.03004 | First VOA construction in Deligne category; Zeng is GLZ coauthor |
| Etingof 1401.6321, 1407.0373 | Foundation for complex-rank rep theory |
| Kalinov 1906.07905 | Yangians in Deligne category (connects to DK programme) |
| Nishinaka (already cited for envelope) | Factorization envelope; precursor to Zeng's categorical construction |

---

## 9. Verdict

### 9.1 The Proposed Bridge Does Not Work

The hypothesis that Deligne categories could bridge the real-to-complex
spectral gap is falsified by the following chain of reasoning:

1. Deligne categories interpolate the RANK parameter (dimension of the
   fundamental representation) to complex values.
2. The spectral parameter s in the Eisenstein series / scattering matrix
   is NOT a rank parameter — it is an analytic variable on the automorphic
   side.
3. The structural obstruction (thm:structural-separation) is about the
   relationship between algebraic MC data and the analytic spectral
   decomposition on M_{1,1}. It operates in the s-direction, not the
   rank-direction.
4. The shadow obstruction tower at complex c is already well-defined by rationality
   of its coefficients. Deligne categories add nothing to this extension.
5. A complex-rank KL equivalence, even if proved, would give categorical
   equivalences parametrized by q (a function of level and rank), not by s.

### 9.2 What Deligne Categories Are Good For (in This Programme)

Deligne categories are genuinely useful for:
- Proving uniform-in-rank properties of W_N families
- Constructing the W_{infinity} / large-N limit rigorously
- Extending Kalinov's Yangian classification to the DK programme
- Providing a categorical framework for studying rank-stability

These are real mathematical applications, but they address the ALGEBRAIC
structure of the shadow obstruction tower, not the ARITHMETIC interface with zeta zeros.

### 9.3 The Genuine Obstruction Remains

The arithmetic programme's structural separation theorem
(thm:structural-separation) proves that the MC element exhausts the
algebraic content of the arithmetic interface at genus 1. The remaining
zero-location question requires either:
- Higher-genus input (complex saddle points at g >= 2), or
- Genuinely analytic input external to the MC equation, or
- The Langlands programme (automorphy, functoriality, converse theorems)

Deligne categories provide none of these. They are an algebraic tool,
and the obstruction is the boundary between algebraic and analytic.

---

## 10. Falsification Checklist (Beilinson Protocol)

| Claim | Status | Reason |
|-------|--------|--------|
| Deligne categories extend shadow obstruction tower to complex rank | TRIVIALLY TRUE but VACUOUS: shadow obstruction tower is already rational in c | No new content |
| Complex-rank KL equivalence would see zeta zeros | FALSE: KL parameter q depends on (k,t), not on spectral s | Orthogonal parameters |
| Epstein zeta at complex c has new analytic properties | PARTIALLY TRUE: branch cuts, convergence issues, Davenport-Heilbronn | But these are OBSTRUCTIONS, not tools |
| Deligne categories bridge real spectral to complex spectral | FALSE: rank interpolation != spectral continuation | Structural type mismatch |
| The c-parameter IS a spectral parameter | FALSE: c parametrizes a FAMILY of algebras; s parametrizes the Eisenstein series | Different roles |
| Zeng's VOA-in-Deligne-category construction helps | POTENTIALLY for W_N uniformity; NOT for arithmetic interface | Algebraic, not analytic |

---

## Sources

- [Zeng, "Large N Vertex Algebras via Deligne Category"](https://arxiv.org/abs/2503.03004)
- [Etingof, "Representation theory in complex rank, I"](https://arxiv.org/abs/1401.6321)
- [Etingof, "Representation theory in complex rank, II"](https://arxiv.org/abs/1407.0373)
- [Kalinov, "Finite-Dimensional Representations of Yangians in Complex Rank"](https://academic.oup.com/imrn/article-abstract/2020/20/6967/5325786)
- [Kannan-Kanungo, "Representation Theory of the Twisted Yangians in Complex Rank"](https://arxiv.org/abs/2505.06463)
- [Entova-Aizenbud-Serganova, "Deligne categories and the limit of categories Rep(GL(m|n))"](https://arxiv.org/abs/1511.07699)
- [An Introduction to Deligne Categories](https://arxiv.org/html/2404.08689)
- [Deligne Categories and Representations of the Finite General Linear Group](https://link.springer.com/article/10.1007/s00031-023-09840-1)
- [Gaitsgory, "A conjectural extension of the Kazhdan-Lusztig equivalence"](https://arxiv.org/abs/1810.09054)
