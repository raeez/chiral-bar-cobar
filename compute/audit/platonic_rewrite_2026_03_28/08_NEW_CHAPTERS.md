# BLUEPRINTS FOR NEW CHAPTERS

---

## VOL I, CHAPTER 8: "THE OPEN SECTOR"

### Position in the manuscript
After Chapter 7 (Chiral Koszul duality), before Chapter 9 (Chiral modules).
This is the hinge chapter of the entire monograph: the point where the
closed theory opens into the open/closed theory.

### Estimated length: 40 pages

### Section-by-section blueprint

**8.1 A_infty-chiral algebras (5 pages)**

  Definition 8.1.1. An A_infty-chiral algebra is a cochain complex (A, Q)
  with holomorphic derivation d, unit 1, and operations

      m_k: A^{tensor k} -> A((lambda_1))...((lambda_{k-1})), |m_k| = 1-k

  satisfying sesquilinearity, unitality, and the planar A_infty identities
  with spectral substitution.

  State the identities explicitly. Write out the n=1, n=2, n=3 cases.
  Note: a strict chiral algebra has m_k = 0 for k >= 3. The A_infty
  structure is the homotopy refinement.

  Relate to the bar complex: the A_infty data is equivalent to a square-zero
  coderivation on the cofree conilpotent coalgebra T^c(sA).

  Example: the free A_infty-chiral algebra (m_1 = Q, m_2 = product, rest zero).
  Example: the Heisenberg (m_2 = k lambda, rest zero).
  Non-example: Virasoro has m_3 != 0 on the transferred minimal model.

**8.2 The local chiral Swiss-cheese operad (3 pages)**

  Definition 8.2.1. The local chiral Swiss-cheese operad SC^{ch,top} is the
  two-colored operad with:
    SC(ch^k; ch) = FM_k(C)
    SC(ch^k, top^m; top) = FM_k(C) x E_1(m)
    SC(top^m; ch) = empty (no open-to-closed operations)

  Theorem 8.2.2 (Recognition, proved in Vol II). Algebras over C_*(W(SC^{ch,top}))
  are equivalent to local holomorphic-topological prefactorization algebras
  on rectangles in C x R.

  Reference Vol II for the proof. State only the result here.

**8.3 Chiral Hochschild cochains (5 pages)**

  Definition 8.3.1. The chiral endomorphism operad:

      End^{ch}_A(n) := Hom(A^{tensor n}, A((lambda_1))...((lambda_{n-1})))

  Define partial composition o_i with spectral substitution Lambda_i.
  Show associativity from associativity of block substitution.

  Definition 8.3.2. The chiral Hochschild cochain complex:

      C^n_ch(A,A) := End^{ch}_A(n+1)[-n]

  Definition 8.3.3. Brace operations:

      f{g_1,...,g_r} := sum_{i_1 < ... < i_r} +/- f o_{i_r} g_r ... o_{i_1} g_1

  Definition 8.3.4. Gerstenhaber bracket:

      [f,g] := f{g} - (-1)^{(|f|-1)(|g|-1)} g{f}

  Definition 8.3.5. Differential:

      delta f := [m, f], where m := m_1 + m_2 + m_3 + ...

**8.4 The chiral brace algebra theorem (5 pages)**

  Theorem 8.4.1. (C^bullet_ch(A,A), delta, {-}) is a brace dg algebra.
  Hence [-, -] is a dg Lie bracket, and HH^bullet_ch(A) is a Gerstenhaber algebra.

  Proof. The brace identity:
    f{g_1,...,g_r}{h_1,...,h_s} = sum +/- f{h_1,..., g_1{...}, ..., g_r{...}, ..., h_s}
  Both sides enumerate the same set of planar rooted trees with spectral
  variable assignments. Spectral variables compose by consecutive block
  substitution; associativity is operadic associativity of o_i.

  delta^2 = [m, [m, -]] = (1/2)[[m,m], -] = 0 because the A_infty identities
  are exactly [m,m] = 0.

  dg Lie: standard consequence of brace identities. QED.

**8.5 The chiral Deligne-Tamarkin theorem (5 pages)**

  Definition 8.5.1. A local chiral Swiss-cheese pair (B, A) consists of:
    - A: an A_infty-chiral algebra (open color)
    - B: a brace algebra (closed color)
    - Mixed operations mu_{p;q}: B^{tensor p} tensor A^{tensor q} -> A((lambda))
      compatible with braces on B and A_infty on A.

  Definition 8.5.2. The universal thickening:
    U(A) := (C^bullet_ch(A,A), A)
  with closed color C^bullet_ch carrying braces, open color A with A_infty,
  and mixed action by evaluation: ev(f; a_1,...,a_n) := f(a_1,...,a_n).

  Theorem 8.5.3 (Chiral Deligne-Tamarkin-Swiss-cheese).
  U(A) is a local chiral Swiss-cheese pair. It is initial among all such
  pairs with fixed open color A: for any (B, A) there is a unique morphism
  Phi: B -> C^bullet_ch(A,A) compatible with the action on A.

  Proof of Swiss-cheese structure: evaluation is compatible with braces and
  A_infty. The Swiss-cheese identities are:
    (f{g}) . a = f . (g . a)
    delta(f . a) = (delta f) . a +/- f . (delta a)
  These follow from the brace identities and the A_infty identities.

  Proof of initiality: Define Phi(b)_n(a_1,...,a_n) := mu_{1;n}(b; a_1,...,a_n).
  This is a chiral cochain by sesquilinearity. Compatibility with braces:
  the codimension-one Swiss-cheese identity where one closed input bubbles
  into another before acting on open inputs. Uniqueness: a morphism over A
  is determined by what a closed element does to arbitrary strings of open inputs.

  Remark: this is the chiral analogue of the Kontsevich-Soibelman generalized
  Deligne conjecture: every d-algebra has a universal (d+1)-algebra acting on it.

**8.6 Bulk = derived center (3 pages)**

  Corollary 8.6.1. For a cyclic open factorization dg-category C_op with
  compact generator b, the derived center is:

      Z_ch(C_op) := RHom_{Fun(C_op, C_op)}(Id, Id) ~ C^bullet_ch(A_b, A_b)

  Proof. The identity functor is represented by the diagonal A_b-bimodule.
  Its derived endomorphisms are Hochschild cochains. Morita equivalence
  identifies endofunctor categories for different generators.

  Corollary 8.6.2 (Morita invariance). Z_ch(C_op) is independent of the
  choice of compact generator.

**8.7 Why 2d chiral data produces 3d HT structure (3 pages)**

  The center theorem is the conceptual explanation:
  - A boundary algebra A is a 1d-holomorphic / 0d-topological object
  - Its derived center C^bullet_ch(A,A) is the universal 2d-hol / 1d-top bulk
  - The pair (C^bullet_ch(A,A), A) is a local 3d HT bulk-boundary system

  The bar coalgebra Bar(A) is the open-sector coalgebra model:
  - Differential = holomorphic factorization
  - Coproduct = topological factorization (along R)
  - Together: Swiss-cheese algebra on FM_k(C) x Conf_k(R)

  The bar/center distinction:
  - Bar/cobar: represents twisting morphisms (coupling space)
  - Center/cochains: IS the acting bulk
  - These are compatible but distinct

  Physical realization: Khan-Zeng construct a 3d HT gauge theory from a PVA.
  Gauge invariance = lambda-Jacobi identity. Virasoro element -> topological.

**8.8 Tangential log curves and the global open sector (4 pages)**

  Definition 8.8.1. A tangential log curve is a triple (X, D, tau) where
  X is a smooth algebraic curve, D = {p_1,...,p_r} is a finite reduced
  divisor, and tau_{p_i} is a nonzero tangent vector at each p_i.

  The real oriented blowup X~_D produces boundary circles S^1_{p_i}.
  The tangential basepoint gives intervals I_{p_i} = S^1_{p_i} \ {tau_{p_i}} ~ R.

  Definition 8.8.2. The open/closed factorization dg-category on (X,D,tau)
  is a constructible dg-cosheaf on Ran^{oc}(X,D,tau) satisfying factorization,
  holomorphicity, local constancy, local SC model, and Weiss descent.

  This is a DEFINITION. Constructing specific examples is a theorem.

  Theorem 8.8.3. A chosen compact generator b in C(J) produces an
  A_infty-chiral algebra A_b = RHom(b,b).

  Corollary 8.8.4. Perf(A_b) ~ Perf(A_{b'}) for different generators.

**8.9 The one-step Jacobi coalgebra (3 pages)**

  Construction 8.9.1. Given F: (A^n, p) -> (A^r, 0), define:
    J_{F,p} := (S^c(sU + R), b_F)
  where b_F is the coderivation from Taylor coefficients of F.

  Proposition 8.9.2. Omega(J_{F,p}) is the exact pointed line algebra.

  Explicit model: K^{gr}_{F,p} = k[c_alpha] tensor Lambda(lambda_i) with
  m_n from d^n F / dx^n.

  Three subexamples: F=0, F=x^2, F=x^3.

**8.10 Boundary-linear Landau-Ginzburg (4 pages)**

  Theorem 8.10.1. For W(x,y) = <y, F(x)>, the boundary algebra is:
    A_F = (k[[x]] tensor Lambda(eta), d eta = F(x))
  and
    Z^{ch}_der(A_F) ~ O(dCrit(W)) ~ O(T*[-1] Z^{der}_F)

  Proof. By dg HKR. For the boundary-linear superpotential, dCrit(W) = T*[-1] Z^{der}_F.

  Example: F(x) = x^2 (node). Example: F(x) = x^3 (cusp).
  Example: F(x_1,...,x_n) = sum x_i^2 (quadratic hypersurface).

---

## VOL I, CHAPTER 38: "THE STAIRCASE OF EXAMPLES"

### Position
Last chapter of Part II (Standard Landscape), after genus expansions.

### Estimated length: 15 pages

### Blueprint
See 09_EXAMPLE_STAIRCASE.md for full details.

---

## VOL II, CHAPTER 6: "TANGENTIAL LOG CURVES AND THE GLOBAL OPEN SECTOR"

### Position
Part I of Vol II, after the center theorem chapter.

### Estimated length: 20 pages

### Blueprint

  6.1 Tangential log curves: full definition, examples (P^1 with n punctures,
      elliptic with one puncture, higher genus with marked points).

  6.2 Real oriented blowup: construction, boundary circles, tangential
      linearization to intervals.

  6.3 Mixed configuration spaces: formal definition, examples at low n.
      Products of Conf(X \ D) and Conf^{ord}(I_p).

  6.4 Mixed Ran space: colimit construction, coloring, factorization structure.

  6.5 Open/closed factorization dg-category: the five axioms (factorization,
      holomorphicity, local constancy, local SC model, Weiss descent).

  6.6 Boundary algebra from compact generator: theorem + proof.

  6.7 Morita invariance: theorem + proof.

  6.8 Global center: Z_ch(C_op) on the curve. Relation to Vol I bulk.

---

## VOL II, CHAPTER 7: "ONE-STEP JACOBI COALGEBRA AND EXACT MODELS"

### Position
Part I of Vol II, after the global open sector chapter.

### Estimated length: 15 pages

### Blueprint

  7.1 The one-step Jacobi coalgebra: construction from boundary equations.

  7.2 Cobar algebra = exact pointed line algebra. Explicit generators.

  7.3 The A_infty model: higher products from Taylor coefficients.
      Explicit formulas.

  7.4 Free / quadratic / cubic subexamples.

  7.5 Boundary-linear LG: W = <y, F(x)>. Bulk = O(dCrit(W)).

  7.6 Koszul duality in the exact sector: the duality between J_{F,p}
      and the Koszul dual boundary algebra.

---

## VOL II, CHAPTER 14: "MODULAR COMPLETION FROM OPEN-SECTOR TRACES"

### Position
Part III of Vol II, after line operators.

### Estimated length: 25 pages

### Blueprint

  14.1 Cyclic structure on open factorization category.
       Calabi-Yau trace. Nondegeneracy. Compatibility with factorization.

  14.2 Annulus = Hochschild chains.
       Excision proof. Cut circle into interval + collar. Cyclic bar construction.

  14.3 The modular cooperad on bordered log-FM.
       Definition via chains on compactified moduli of bordered stable curves.
       The four types of codimension-one strata.

  14.4 The modular twisting morphism.
       Theta_C: C^{oc,log}_{mod} -> End(Z_ch(C_op), C_op).

  14.5 The modular Maurer-Cartan equation.
       d Theta + (1/2)[Theta, Theta] + Delta_{clutch}(Theta) = 0.
       Proof from Stokes on compactified 1-dimensional families.

  14.6 Modularity = trace + clutching.
       The hierarchy: chiral -> open/SC -> cyclic -> traced -> ribbon -> modular.
       Each level is a trace shadow of the previous.

  14.7 The ribbon/'t Hooft bridge.
       't Hooft expansion = open-sector trace on ribbon modular operad.
       Matrix realization. N^{chi(Sigma_Gamma)} weighting.
       Connection to Vol I E_1 modular Koszul duality.
