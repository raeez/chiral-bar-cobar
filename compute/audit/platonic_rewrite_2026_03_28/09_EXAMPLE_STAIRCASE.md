# THE STAIRCASE OF EXAMPLES — IN FULL DETAIL

This is the blueprint for Vol I Chapter 38 ("The staircase of examples")
and Vol II Part IV (Chapters 15-20).

---

## The organizing principle

The examples are not a list. They form a staircase: each one reveals a new
structural layer of the theory that was invisible at the previous level.
The staircase is the theory's proof of concept, its computational backbone,
and its source of conceptual clarity.

The structural layers revealed by successive examples:

| Step | Example | New layer revealed |
|------|---------|-------------------|
| 0 | Free multiplet | Bar complex exists; d^2 = 0; center = polyvectors |
| 1 | Heisenberg H_k | First nontrivial spectral layer (lambda-bracket); abelian CS; Laplace kernel r(z) = hbar/z |
| 2 | Cubic LG | First genuine m_3; geometric degree counting forces m_4 = 0; finite A_infty truncation |
| 3 | Affine sl_2 | Nonabelian current algebra; 27 Jacobi triples; exact complementarity under FF; 3d CS |
| 4 | Virasoro | Infinite tower; wheel combinatorics; chiral Cartan formula; topological enhancement |
| 5 | W_3 | Composite nonlinearity; quartic resonance; category beyond linear; non-polynomial complementarity |

---

## STEP 0: FREE MULTIPLET

### The A_infty data
Fields: phi (degree 0), psi (degree 1). BRST: Q phi = psi, Q psi = 0.

    m_1(phi) = psi,    m_1(psi) = 0
    m_2(a,b) = ab       (ordinary product)
    m_k = 0             (k >= 3)

### The bar complex
    b[phi] = [psi],    b[psi] = 0
    b[phi|phi] = [psi|phi] - [phi|psi]

No merge terms beyond multiplication. Everything strict at tree level.

### The center
    C^bullet_ch(A_free, A_free) ~ k[x_i^{(m)}, psi_{i,m}]

Free polyvectors. Zero differential. HKR is already a quasi-isomorphism.

### The open sector
Deconcatenation coproduct: Delta[phi|psi|phi] = 1 tensor [phi|psi|phi]
+ [phi] tensor [psi|phi] + [phi|psi] tensor [phi] + [phi|psi|phi] tensor 1.

### Genus one
    kappa_free = 1/2,    F_1 = 1/48

### What this step proves
The bar direction EXISTS before any nonlinear interaction. The center is
trivially computable. Genus one is already nontrivial even though tree level
is strict.

---

## STEP 1: HEISENBERG H_k

### The PVA bracket
    {J_lambda J} = k lambda

### The 3d action (Khan-Zeng)
    S = int_{R x C} dz (eta (d_t + dbar) phi + (k/2) eta d_z eta)

Gauge invariance is automatic (abelian Jacobi identity).

### The spectral kernel
    r(z) = hbar q_1 q_2 / z

This is the Laplace transform of {J_lambda J} = k lambda:

    r(z) = int_0^infty d lambda e^{-lambda z} (k lambda) = k hbar / z^2

(up to normalization). The simplest spectral data.

### Genus one
    kappa_{H_k} = k/2,    F_1 = k/48

Partition function: Z_1(H_k) = eta(tau)^{-k}.

### Complementarity
    kappa(k) + kappa(-k) = 0,    F_1(k) + F_1(-k) = 0

Anti-symmetric. The cleanest duality witness.

### What this step proves
Nontrivial spectral data can exist while the nonlinear tree layer is still
absent. The Laplace transform dictionary works. Abelian CS is the physical
realization.

---

## STEP 2: CUBIC LANDAU-GINZBURG

### The A_infty data
    W(phi) = (g/3) phi^3

Transferred structure:
    m_1(phi) = psi,    m_2(a,b) = ab,    m_3(a,b,c) = 2g abc
    m_k = 0  (k >= 4)

### Why m_4 = 0: degree counting
For a tree with k external legs and only cubic vertices:
    V = k-2,    E = k-3,    available degree = 2E = 2k-6
    FM dimension = 2(k-1) = 2k-2
    deficit = (2k-2) - (2k-6) = 4 (independent of k)

Never enough degree to produce a top form for k >= 4. Therefore m_4 = 0.

For k=4: V=2, E=1, FM_4 dimension = 6, available = 2. Deficit 4. m_4 = 0.
For k=5: V=3, E=2, FM_5 dimension = 8, available = 4. Deficit 4. m_5 = 0.

### What this step proves
Genuine higher A_infty operations can appear with a GEOMETRIC reason for
finite truncation. This is the perfect toy model: nontrivial m_3, but
m_k = 0 for k >= 4 by configuration-space degree counting, not by wishful
truncation.

---

## STEP 3: AFFINE sl_2

### The PVA bracket
    {J^a_lambda J^b} = epsilon^{abc} J^c + k delta^{ab} lambda

Explicitly:
    {J^1_lambda J^2} = J^3,   {J^2_lambda J^3} = J^1,   {J^3_lambda J^1} = J^2
    {J^a_lambda J^a} = k lambda   (a = 1,2,3)

### Jacobi verification (one triple)
    {J^1_lambda {J^2_mu J^3}} = {J^1_lambda J^1} = k lambda

    {{J^1_lambda J^2}_{lambda+mu} J^3} + {J^2_mu {J^1_lambda J^3}}
      = {J^3_{lambda+mu} J^3} + {J^2_mu (-J^2)}
      = k(lambda + mu) - k mu = k lambda.  CHECK.

The compute layer verifies all 27 ordered triples.

### The 3d action (Khan-Zeng)
    S = int dz (B_a (d_t + dbar) A^a + (1/2) f_{abc} B_a A^b A^c + (k/2) kappa_{ab} A^a d_z A^b)

For k != 0, this becomes Chern-Simons after the field redefinition
A~_a = A_a + (1/k) kappa_{ab} B^b dz.

### Sugawara stress tensor
    T = (1/(2(k+2))) sum_{a=1}^3 :J^a J^a:,    c = 3k/(k+2)

### Genus one
    kappa = 3(k+2)/4,    F_1 = (k+2)/32

### Complementarity (Feigin-Frenkel)
Under k -> -k-4:
    kappa(k) + kappa(-k-4) = 0,    F_1(k) + F_1(-k-4) = 0

### The classical line kernel
    r(z) = Omega/z,    Omega = (1/2) h tensor h + e tensor f + f tensor e

### What this step proves
Nonabelian current algebra, 3d CS geometry, and exact complementarity
already coexist at low complexity. The line kernel is genuinely matrix-valued.

---

## STEP 4: VIRASORO

### The PVA bracket
    {T_lambda T} = dT + 2 lambda T + (c/12) lambda^3

### The chiral Cartan formula
For f in C^bullet_ch(Vir_c, Vir_c):

    [T, f] = d f + delta(iota_T f)

Hence [d] = 0 in HH^bullet_ch(Vir_c). An inner Virasoro element makes
holomorphic translation exact in cohomology.

This is the chain-level version of Khan-Zeng's theorem: a Virasoro element
upgrades HT to topological.

### Wheel combinatorics
For the one-loop all-cubic wheel at arity k:
    n_3 = k,    E = k,    L = 1,    |Aut| = 2k

This is a cycle C_k (every cubic vertex has degree 2).

At k=4: 1 pure wheel + 4 one-ghost insertions + 10 two-ghost insertions.
This is the habitat of the quartic resonance class.

### The higher operation m_3
    m_3(T,T,T; lambda_1, lambda_2) = d^2 T + (2 lambda_1 + 3 lambda_2) dT
      + 2 lambda_2 (2 lambda_1 + lambda_2) T + (c/12) lambda_2^3 (2 lambda_1 + lambda_2)

From Virasoro onward, the tower is infinite. No finite truncation.

### Genus one
    kappa_Vir = c/2,    F_1 = c/48

Vacuum character: chi_Vir(tau) = q^{-c/24}(1 + q^2 + q^3 + 2q^4 + ...)

### Complementarity
Under c -> 26 - c:
    kappa(c) + kappa(26-c) = 13,    F_1(c) + F_1(26-c) = 13/24

Self-dual at c = 13, NOT c = 26.

### What this step proves
(a) Wheel combinatorics force an infinite higher tower.
(b) The chiral Cartan formula is the chain-level mechanism for topological
    enhancement.
(c) Virasoro is where ribbon/modular correction stabilizes.
(d) The complementarity constant 13 is a structural number, not a coincidence.

---

## STEP 5: W_3

### The PVA brackets
    {T_lambda T} = dT + 2 lambda T + (c/12) lambda^3
    {T_lambda W} = dW + 3 lambda W
    {W_lambda T} = 2 dW + 3 lambda W

    {W_lambda W} = (c/360) lambda^5 + (1/3) T lambda^3 + (1/2)(dT) lambda^2
      + (beta_2 Lambda + (3/10) d^2 T) lambda + (beta_2/2)(d Lambda) + (1/15) d^3 T

where:
    Lambda = :TT: - (3/10) d^2 T
    beta_2 = 16/(22 + 5c)

### Why composite fields are forced
The bracket {W_lambda W} does NOT close in the linear span {T, W, dT, dW, ...}.
It creates the QUADRATIC composite Lambda = :TT: - (3/10) d^2 T.

Without Lambda, the Jacobi identity FAILS. Therefore:
- Binary data alone does not close the algebra.
- Composite nonlinear fields are algebraically necessary, not optional.
- The open category for W_3 is genuinely beyond modules over a single linear algebra.

### The absence of lambda^4
In {W_lambda W}, there is no lambda^4 term. This is forced by conformal weight:
    |W| = 3, so {W_lambda W} has total weight 6.
    lambda^4 would contribute weight 4 from lambda and needs weight 2 from fields.
    But there is no quasi-primary of weight 2 in the sector. So the coefficient is
    uniquely zero.

### Genus one
    kappa_{W_3} = 5c/6,    F_1 = 5c/144

### Complementarity
Under c -> 100 - c:
    kappa(c) + kappa(100-c) = 250/3
    F_1(c) + F_1(100-c) = 125/36

### What this step proves
(a) Quadratic/Lie-type descriptions are insufficient.
(b) Composite fields are structurally necessary.
(c) The quartic resonance class is the first genuinely nonlinear shadow.
(d) The theory ceases to be even approximately linear at the W_3 level.

---

## THE UNIFIED NARRATIVE (Vol I Chapter 38)

The staircase tells one story in six voices:

**The complexity hierarchy:**
  strict -> spectral -> first m_3 -> nonabelian -> infinite tower -> composite

**The shadow depth hierarchy:**
  G (Gaussian, r_max=2) -> L (Lie, 3) -> C (contact, 4) -> M (mixed, infty)

**The complementarity hierarchy:**
  kappa + kappa' = 0 (Heis, KM) -> 13 (Vir) -> 250/3 (W_3) -> ...

**The convergence hierarchy:**
  terminates at 2 (Heis) -> 3 (KM) -> 4 (betagamma) -> infty (Vir, W_3)

**The center hierarchy:**
  free polyvectors -> Koszul dual -> dCrit -> nonabelian dCrit -> ...

**The 3d action hierarchy:**
  free -> abelian CS -> cubic LG -> nonabelian CS -> topological -> non-polynomial

Each row of each hierarchy is computed, not conjectured. The staircase is
the theory's experimental verification.

---

## CROSS-REFERENCES

Vol I Chapter 38 should cross-reference:
  - Vol I Chapter 8 (open sector) for the center computations
  - Vol I Chapters 21-37 for the individual example chapters
  - Vol II Chapters 15-20 for the detailed 3d computations
  - Vol I Chapter 16 for shadow depth classification
  - Vol I Chapter 18 for shadow metric and growth rate

Vol II Chapters 15-20 should cross-reference:
  - Vol II Chapter 5 (center theorem) for the theoretical foundation
  - Vol II Chapter 7 (Jacobi coalgebra) for the LG examples
  - Vol I example chapters for the closed-sector computations
  - Each other, for the staircase narrative
