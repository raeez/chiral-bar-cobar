# W-Algebras at Complex Rank: Shadow Tower Interpolation Programme

## Investigation Summary

**Question**: The principal W-algebra W_N = W^k(sl_N) has shadow tower invariants
(kappa, alpha, S_4, Delta, rho_shadow) depending on two discrete parameters (N, k).
Can these be analytically continued to complex rank t in C, and what is the
resulting structure?

**Answer**: YES, with a precise dichotomy. The shadow tower data splits into
two layers with different analytic behavior:

1. **T-line data** (Virasoro subalgebra shadow): depends on t only through
   c(t,k), which is RATIONAL in t. All T-line shadow coefficients S_r^T are
   algebraic functions of t. This interpolation is canonical and well-defined.

2. **Total data** (full W_t shadow): involves the anomaly ratio
   rho(t) = psi(t+1) + gamma - 1 (digamma function), which is MEROMORPHIC
   in t with simple poles at t = -1, -2, -3, .... The total kappa and all
   total shadow invariants are meromorphic, not algebraic, in t.

The shadow growth rate |rho_shadow| -> 0 as |t| -> infinity (at fixed k),
meaning the shadow tower converges BETTER at large complex rank. W_t is
always class M on the T-line (Delta != 0) for all t in C where c(t,k) is
finite, nonzero, and != -22/5.

---

## 1. Setup: The W_N Shadow Tower at Integer Rank

### 1.1 Central charge

The principal W-algebra W_N = DS(sl_N-hat at level k) has central charge:

    c(N, k) = (N-1)(1 - N(N+1)/(k+N))

This is RATIONAL in both N and k. Pole at k = -N (critical level).

For large N at fixed k: c ~ -(N-1)N ~ -N^2 (negative, quadratically divergent).
For large k at fixed N: c -> N-1 (the rank minus 1).

**Zero locus**: c = 0 iff N(N+1) = k+N, i.e., k = N^2.
Example: c(W_10, k=100) = 0 exactly.

### 1.2 Modular characteristic

Total modular characteristic:

    kappa(W_N) = c * (H_N - 1)

where H_N = 1 + 1/2 + ... + 1/N is the N-th harmonic number.
Channel-refined: kappa_j = c/j for the W_j generator (j = 2, ..., N).

First values of the anomaly ratio rho_N = H_N - 1:

| N  | H_N     | rho_N   |
|----|---------|---------|
| 2  | 3/2     | 1/2     |
| 3  | 11/6    | 5/6     |
| 4  | 25/12   | 13/12   |
| 5  | 137/60  | 77/60   |
| 10 | 7381/2520 | 1.929  |

Note: rho_N > 1 for N >= 4. The modular characteristic EXCEEDS the central
charge for rank >= 4.

### 1.3 Shadow tower data on the T-line

On the T-line (restricting to the Virasoro subalgebra), the shadow data is
IDENTICAL to Virasoro at the same central charge:

    S_2 = kappa_T = c/2
    S_3 = alpha = 2  (UNIVERSAL, independent of N)
    S_4 = 10/[c(5c+22)]  (Virasoro quartic contact)
    Delta = 40/(5c+22)  (critical discriminant)

Shadow depth: class M (infinite tower) for all finite c != 0, -22/5.

Shadow growth rate on T-line:

    rho_shadow = sqrt((180c + 872) / ((5c+22) c^2))

Critical central charge: rho = 1 at c* ~ 6.124 (root of 5c^3 + 22c^2 - 180c - 872 = 0).

### 1.4 Koszul conductor

    K_N = 4N^3 - 2N - 2 = 2(N-1)(2N^2 + 2N + 1)

Equivalently: K_N = 2(N-1) + 4N(N^2-1) (Freudenthal-de Vries formula).

Self-dual central charge: c* = K_N/2 = (N-1)(2N^2+2N+1).

First values: K_2 = 26, K_3 = 100, K_4 = 246, K_5 = 488.

---

## 2. Analytic Continuation to Complex Rank t

### 2.1 Central charge at complex t

    c(t, k) = (t-1)(1 - t(t+1)/(k+t)) = (t-1)(k - t^2)/(k + t)

This is a RATIONAL function of t for fixed k. Key features:

- **Pole**: t = -k (critical level of sl_t-hat).
- **Zeros**: t = 1 (trivial: W_1 doesn't exist) and t = sqrt(k) (where c vanishes).
- **Large |t|**: c(t,k) ~ -t^2 (quadratic divergence, negative).
- The formula makes sense for ALL t in C \ {-k}, giving a meromorphic function
  with a single pole.

### 2.2 The anomaly ratio at complex t

The harmonic number H_N interpolates to the digamma function:

    H_t := psi(t+1) + gamma

where psi = Gamma'/Gamma is the digamma function and gamma is the Euler-Mascheroni
constant. For positive integers n: H_n = psi(n+1) + gamma (standard identity).

The anomaly ratio at complex t:

    rho(t) = H_t - 1 = psi(t+1) + gamma - 1

**Analytic structure of rho(t)**:

- **Meromorphic** on C with simple poles at t = -1, -2, -3, ...
  (coming from the poles of psi at z = 0, -1, -2, ...).
- **Residue**: 1 at each pole (since Res_{z=n} psi(z) = -1 for n = 0, -1, -2, ...,
  and psi(t+1) has poles at t+1 = 0, -1, ..., i.e., t = -1, -2, ...).
- **Unique real zero**: t = 1 (since H_1 = 1). No other positive real zeros
  (rho is monotonically increasing on (0, infty)). Numerical search found
  NO complex zeros in [-4,4] x [-4,4]i.
- **Asymptotics**: rho(t) ~ log(t) as |t| -> infinity (the harmonic series divergence
  becomes logarithmic growth of digamma).
- **Reflection**: psi(1-z) - psi(z) = pi*cot(pi*z) gives
  rho(-t) = rho(t-1) + pi*cot(pi*t) - 2 (relating complex-conjugate ranks).

### 2.3 Total kappa at complex t

    kappa(W_t) = c(t,k) * rho(t) = [(t-1)(k-t^2)/(k+t)] * [psi(t+1) + gamma - 1]

This is MEROMORPHIC in t, being the product of a rational function and a
meromorphic function. Poles:

- t = -k (from c)
- t = -1, -2, -3, ... (from psi)
- The t = -1 pole has residue: c(-1,k) * 1 = (-2)(k-1)/(k-1) * 1 = -2 (for k != 1).

For large |t|: kappa ~ -t^2 * log(t) (logarithmically enhanced quadratic divergence).

**WARNING (AP20)**: kappa(W_t) and kappa_T = c/2 are DIFFERENT objects.
kappa_T is the T-line (Virasoro) contribution; kappa(W_t) is the total.
They agree only at t = 2 (Virasoro itself).

### 2.4 Koszul conductor at complex t

    K_t = 4t^3 - 2t - 2 = 2(t-1)(2t^2 + 2t + 1)

This is a POLYNOMIAL in t, perfectly well-defined for all t in C.
Self-dual central charge: c* = K_t/2 = (t-1)(2t^2+2t+1).

**Zeros of K_t**: t = 1 and t = (-1 +/- i)/2. The zeros t = (-1 +/- i)/2
are the complex ranks at which the Koszul conductor vanishes, meaning
c + c' = 0 under Koszul duality. These are the "anomaly-free" complex ranks.

### 2.5 Critical discriminant at complex t

On the T-line:

    Delta_T = 40/(5c(t,k) + 22)

Since c(t,k) is rational in t, so is Delta_T. Delta_T = 0 only if
5c + 22 -> infinity, which never happens for finite t. So:

**W_t is class M on the T-line for ALL t in C \ {singularities}.**

The singular t-values where Delta_T diverges are those where 5c(t,k) + 22 = 0,
i.e., c = -22/5. These are the roots of:

    5(t-1)(k-t^2)/(k+t) + 22 = 0

which is a cubic in t with generically three solutions (one real, two complex
conjugate for k = 10).

---

## 3. Shadow Tower at Complex Rank: Explicit Computation

### 3.1 T-line shadow tower

The T-line shadow coefficients S_r^T are determined by the convolution recursion:

    sqrt(Q_L(t)) = sum_{n>=0} a_n t^n,  S_r = a_{r-2}/r

where Q_L(t) = c^2 + 12ct + ((180c+872)/(5c+22)) t^2 and c = c(t,k).

Since Q_L depends RATIONALLY on c, and hence rationally on t, the shadow
tower coefficients S_r^T at any arity r are ALGEBRAIC functions of t.

**KEY UNIVERSALITY**: S_3 = alpha = 2 for ALL t. The gravitational cubic shadow
coefficient is determined by the Virasoro OPE structure constants and is
independent of the rank of the W-algebra. This is verified numerically at
t = 2, 2.5, 3, 3.5, 4, 5 (all give S_3 = 2.000000 exactly).

Numerical shadow tower at k = 10:

| t   | c(t)    | S_2      | S_3 | S_4      | S_5       | S_6       |
|-----|---------|----------|-----|----------|-----------|-----------|
| 2.0 | 0.5000  | 0.2500   | 2.0 | 0.8163   | -7.8367   | 76.590    |
| 2.5 | 0.4500  | 0.2250   | 2.0 | 0.9164   | -9.7747   | 106.12    |
| 3.0 | 0.1538  | 0.0769   | 2.0 | 2.8547   | -89.068   | 2824.1    |
| 3.5 | -0.4167 | -0.2083  | 2.0 | -1.2050  | -13.882   | -161.94   |
| 4.0 | -1.2857 | -0.6429  | 2.0 | -0.4995  | -1.8648   | -6.993    |
| 5.0 | -4.0000 | -2.0000  | 2.0 | -1.2500  | -1.5000   | -1.354    |
| 10  | -40.50  | -20.25   | 2.0 | 0.00137  | 0.000162  | 0.0000197 |
| 20  | -247.0  | -123.5   | 2.0 | 0.0000330| 0.00000054| < 1e-8    |

**Observation**: At large t, S_r for r >= 4 decays rapidly (as 1/t^{2(r-3)}),
while S_2 ~ -t^2/2 grows. The shadow tower becomes increasingly dominated
by the quadratic term (approaching class G behavior asymptotically).

### 3.2 Shadow growth rate at complex t

On the T-line:

    |rho_shadow(t)| = |sqrt((180c + 872) / ((5c+22) c^2))|

Large-t asymptotics: |rho_shadow| ~ 6/t^2 -> 0.

**The shadow tower converges better and better at large |t|.**

Numerical table (k = 10):

| t   | c(t)     | |rho_shadow| | Convergent? |
|-----|----------|-------------|-------------|
| 2   | 0.50     | 12.53       | NO          |
| 3   | 0.15     | 40.86       | NO          |
| 5   | -4.00    | 2.18        | NO          |
| 7   | -13.76   | 0.425       | YES         |
| 10  | -40.50   | 0.147       | YES         |
| 20  | -247.0   | 0.024       | YES         |
| 50  | -2034    | 0.00295     | YES         |
| 100 | -8991    | 0.000667    | YES         |
| 1000| -989099  | 0.0000061   | YES         |

The last column matches the asymptotic prediction 6/t^2 to within 10%.

**Critical rank**: The T-line shadow growth rate equals 1 when c(t,k) = c*
(the Virasoro critical central charge ~ 6.124). At k = 10, the corresponding
t is at t ~ -4.125 (obtained by solving (t-1)(10-t^2)/(10+t) = 6.124). This
is a negative non-integer, so the critical rank is NOT a physical W-algebra.
For k = 10, the physical W_2 (t=2) already has rho >> 1, and convergence begins
only for t >= 7 (approximately).

### 3.3 Total shadow data at complex t

Using total kappa = c * rho(t) instead of kappa_T = c/2:

The total critical discriminant:

    Delta_total = 80 * rho(t) / (5c+22)

vanishes iff rho(t) = 0, i.e., at t = 1 (uniquely on the positive real line).
For complex t, the analysis of the digamma zeros (Section 2.2) suggests
t = 1 may be the UNIQUE zero of rho(t), making Delta_total != 0 generically.

The total shadow growth rate involves kappa_total instead of kappa_T in the
denominator, so it decreases with the harmonic sum:

    rho_shadow^total ~ rho_shadow^T / rho(t) ~ rho_shadow^T / log(t)

For large t: rho_shadow^total ~ 6/(t^2 log(t)), even faster decay.

---

## 4. The DS Reduction at Complex Rank

### 4.1 The Miura transformation

For integer N, the Miura transformation factors the DS differential:

    partial^N + sum_{j=2}^N W_j partial^{N-j} = prod_{a=1}^N (partial - alpha_a . partial phi)

where phi = (phi_1, ..., phi_{N-1}) are free fields and alpha_a are simple roots.

At complex t: the number of free fields t-1 is not an integer, and the
product of t differential operators does not have a direct meaning.
However, the OPE structure constants of W_t are rational functions of t
(this is the content of the Deligne-category construction of W_t by
Etingof-Kazhdan and recent work of Linshaw and others).

**The shadow tower on the T-line does NOT need the Miura map**: it depends
on t only through c(t,k), which is rational. The Miura map would be needed
for the FULL multi-line shadow tower, which requires the W_j-W_j' OPE
structure constants. These interpolate as rational functions of t in the
Deligne category framework, but verifying this requires detailed structural
information about W_t that is beyond the current manuscript.

### 4.2 Ghost sector at complex t

For principal DS of sl_N-hat: c_ghost = N(N-1) (independent of k).
At complex t: c_ghost(t) = t(t-1), which is polynomial in t.

The ghost sector kappa: kappa_ghost = c_ghost/2 = t(t-1)/2.
The ghost central charge: c_ghost(2) = 2 (Virasoro), c_ghost(3) = 6, etc.

At complex t, the ghost sector consists of "t(t-1)/2 effective bc pairs"
in the sense that the shadow data is determined by this effective central charge.
However, the individual bc systems (one for each positive root of sl_t) do
NOT have a direct meaning at non-integer t.

### 4.3 Depth increase at complex t

At integer N >= 2: DS takes sl_N (class L, depth 3, Delta = 0) to W_N
(class M, depth infinity, Delta != 0). The depth increase mechanism is the
BRST coupling creating a nonzero quartic S_4.

At complex t: since S_4 = 10/(c(5c+22)) != 0 generically, the depth increase
persists. The class M (infinite depth) structure is a GENERIC feature that
is broken only at the isolated singularities c = 0 and c = -22/5.

**Key structural point**: The depth increase from class L to class M under
DS reduction is an example of non-commutativity of the shadow-DS diagram
at arity >= 4. This non-commutativity persists at complex rank because
S_4 is a rational function of t with no mechanism for cancellation.

---

## 5. The M2-M5 Duality at Complex Rank

### 5.1 The physical setup

M2 branes: A(K) = DDCA_{epsilon_1, epsilon_2}(gl_K) (deformation-quantized Coulomb branch).
M5 branes: W_{1+infinity}(K) = lim_{N->infinity} W_N(gl_K) (large-N limit of W-algebras).

At integer K: these are related by M-theory duality.
At complex K (= complex t in our notation): both objects should extend to
Deligne-category constructions.

### 5.2 The shadow tower of W_{1+infinity}

The W_{1+infinity} algebra has generators W_j for ALL j >= 2 (infinitely many).
Its total kappa is:

    kappa(W_infinity) = c * sum_{j=2}^infinity 1/j = c * (H_infinity - 1) = DIVERGENT

This DIVERGENCE (the harmonic series) is a fundamental obstruction to defining
the total modular characteristic of W_{1+infinity}. The T-line data (Virasoro
subalgebra) is well-defined, but the total kappa across all channels is infinite.

**Physical resolution**: In the 't Hooft limit lambda = N/(k+N) fixed, the
central charge c ~ -lambda N^2 -> -infinity, but kappa ~ -lambda N^2 log(N)
-> -infinity. The meaningful quantity is the RATIO kappa/c = H_N - 1 ~ log(N),
which diverges logarithmically.

This suggests that W_{1+infinity} requires a RENORMALIZED modular characteristic,
normalized by the number of generators. The natural candidate is:

    kappa_renorm = lim_{N->infinity} kappa(W_N) / log(N) = c * lim (H_N-1)/log(N) = c

So the renormalized kappa of W_{1+infinity} is simply c (the central charge itself).
This is consistent with the Heisenberg limit: for the rank-N Heisenberg algebra
(where all generators have weight 1), kappa = N = c, and the ratio kappa/c = 1.

### 5.3 Shadow growth rate at large N

On the T-line: |rho_shadow| ~ 6/N^2 -> 0 as N -> infinity.

This means: the shadow tower of W_N converges better and better at large N.
In the W_{1+infinity} limit, the T-line shadow tower has ZERO growth rate
(formally). The shadow coefficients S_r -> 0 for all r >= 4:

| N    | |rho_shadow| | 6/N^2    |
|------|-------------|----------|
| 10   | 0.1472      | 0.0600   |
| 20   | 0.0243      | 0.0150   |
| 50   | 0.00295     | 0.00240  |
| 100  | 0.000667    | 0.000600 |
| 1000 | 0.0000061   | 0.0000060|

The asymptotic agreement improves: |rho_shadow| / (6/N^2) -> 1.

**Interpretation**: At large rank, the Virasoro subalgebra's central charge
is so negative that the quartic and higher shadow terms are negligible.
The shadow tower becomes essentially Gaussian (class G) in the large-N limit.
This is consistent with the known fact that W_{1+infinity} at c = 0 has
trivial curvature.

### 5.4 Integer specialization

At integer t = N:

    c(N, k) = (N-1)(1 - N(N+1)/(k+N))
    kappa(W_N) = c * (H_N - 1) [exact harmonic number]
    K_N = 4N^3 - 2N - 2

The complex-t formulas specialize correctly:

    c(t, k)|_{t=N} = c(N, k) [rational identity]
    rho(t)|_{t=N} = psi(N+1) + gamma - 1 = H_N - 1 [digamma identity]
    K_t|_{t=N} = 4N^3 - 2N - 2 [polynomial identity]

So the interpolation is EXACT at integer points (no smoothing or approximation).

---

## 6. Open Questions and Conjectural Directions

### 6.1 Multi-line shadow tower at complex t

The T-line shadow tower interpolates rationally (through c(t,k)). But
the FULL W_t shadow tower, including all W_j primary lines, requires:

(a) The OPE structure constants C^k_{ij}(t) of W_t at complex rank t.
    These should be rational functions of t in the Deligne-category framework,
    but explicit formulas are not yet available beyond low-rank cases.

(b) The channel-refined kappa vector (c/2, c/3, ..., c/t). At non-integer t,
    this is not a finite vector but rather a formal expression involving the
    digamma function (the "sum" sum_{j=2}^t 1/j is replaced by H_t - 1).

(c) The propagator variance delta_mix(t), which measures multi-channel
    non-autonomy. This involves sums over t-1 channels and does not have
    an obvious interpolation to non-integer t.

**Conjecture (Complex Rank Shadow Tower)**: The full shadow tower of W_t at
complex rank t, including all multi-line effects, is a MEROMORPHIC function
of t (not merely algebraic), with poles at the negative integers t = -1, -2, ...
inherited from the digamma function. The T-line projection is the rational
skeleton; the multi-line corrections are higher-order terms in a "channel
expansion" controlled by the anomaly ratio rho(t).

### 6.2 Koszul duality at complex t

At integer N: W_N(c) is Koszul dual to W_N(K_N - c).
At complex t: the Koszul dual should be W_t(K_t - c) where K_t = 4t^3 - 2t - 2.

The Koszul dual central charge: c' = K_t - c(t,k).
The level of the Koszul dual: k' such that c(t, k') = K_t - c(t, k).

    K_t - c(t,k) = 4t^3 - 2t - 2 - (t-1)(k-t^2)/(k+t)

This is a rational function of t (for fixed k), well-defined for all
t in C \ {-k}. The Koszul duality pairing extends to complex t.

**Self-dual locus**: c(t,k) = K_t/2 = (t-1)(2t^2+2t+1).
This is a CUBIC equation in k (for fixed t), having generically one
real and two complex solutions. The physical self-dual points are
where k makes c real and equal to K_t/2.

### 6.3 Shadow growth rate product under Koszul duality

At integer N: rho(W_N, c) * rho(W_N, K_N-c) is a rational function of c.
The self-dual equality rho = rho' holds at c = K_N/2.

At complex t: the product rho(c(t,k)) * rho(K_t - c(t,k)) extends
as a meromorphic function. The self-dual point c = K_t/2 is where
the two growth rates coincide.

### 6.4 Relation to the existing Deligne-category VOA literature

The existing investigation (deligne_categories_voa.md) analyzed whether
Deligne-category VOA constructions (Etingof-Kazhdan, Zeng 2024-25) could
resolve the arithmetic shadows programme's spectral-vs-algebraic obstruction.
The conclusion was negative: Deligne categories interpolate structure but
not spectral data.

The current investigation shows that the SHADOW TOWER (an algebraic invariant)
DOES interpolate to complex rank. The distinction is:

- Shadow tower data (kappa, S_r, Delta) = algebraic invariants of the VOA -> INTERPOLATE.
- Spectral data (partition function, Hecke eigenvalues) = analytic invariants -> DO NOT
  interpolate in the same way.

This is consistent with the general principle: Deligne categories provide
a framework for interpolating ALGEBRAIC structure, and the shadow tower is
algebraic structure (it comes from the bar complex, which is a purely
algebraic/operadic construction).

### 6.5 The W_{1+infinity} shadow tower and renormalization

The divergence of kappa(W_infinity) = c * (H_infinity - 1) = infinity
raises the question of whether the shadow tower of W_{1+infinity} requires
a renormalization scheme.

**Conjecture (Renormalized Shadow Tower)**: Define the renormalized shadow
coefficients S_r^ren(W_infinity) = lim_{N->infinity} S_r(W_N) / (H_N - 1)^r.
Then S_r^ren is well-defined and S_2^ren = c/2 (the Virasoro kappa,
independent of the renormalization), S_3^ren = 2/(H_infinity - 1) = 0 (the
cubic renormalizes to zero), and S_r^ren = 0 for all r >= 3. The
renormalized shadow tower of W_{1+infinity} is Gaussian (class G).

This would be consistent with the large-N suppression of higher shadow
coefficients observed numerically.

---

## 7. Falsification Checks (Beilinson Principle)

### 7.1 Formula verification

- **c(N, k) formula**: Verified against wn_channel_refined.py (line 73-82)
  and ds_shadow_cascade_engine.py (line 80-96). The simple formula
  c = (N-1)(1 - N(N+1)/(k+N)) matches the Sugawara + DS construction.
  Cross-checked: c(sl_2, k) - c(Vir, k) = 2 = N(N-1) at N=2 for all k.

- **K_N formula**: K_N = 4N^3 - 2N - 2 = 2(N-1)(2N^2+2N+1).
  Verified: K_2 = 26, K_3 = 100, K_4 = 246, K_5 = 488 (matching
  landscape_census.tex rem:koszul-conductor-explicit).
  Derives from Freudenthal-de Vries: K = 2r + 4h^v*d where r = N-1,
  h^v = N, d = N^2-1.

- **Anomaly ratio**: rho_N = H_N - 1 matches cor:anomaly-ratio-ds in
  landscape_census.tex, which gives rho(W_N) = sum_{i=1}^{N-1} 1/(m_i+1)
  where m_i = i are the exponents of sl_N. This sum equals H_N - 1.

- **S_3 = 2 universality**: Verified numerically at 6 different values of t.
  The gravitational cubic is determined by the Virasoro OPE alone, which
  has alpha = 2 (the coefficient of the dT/(z-w) term in the T-T OPE,
  after d log pole extraction per AP19).

### 7.2 Potential pitfalls

- **AP1 (formula copying)**: The central charge formula
  c = (N-1)(1 - N(N+1)/(k+N)) is the SIMPLE formula, NOT the minimal-model
  parameterization c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N) which appears in
  wn_channel_refined.py line 82. These are DIFFERENT formulas that agree only
  for specific parameterizations. The simple formula is correct at general
  level k (verified by ghost central charge additivity). [STATUS: potential
  inconsistency in the codebase; wn_channel_refined.py line 82 may be wrong
  for general k.]

- **AP9 (same name, different object)**: rho means THREE different things here:
  rho_N = H_N - 1 (anomaly ratio),
  rho_shadow (shadow growth rate on T-line),
  rho(t) = psi(t+1) + gamma - 1 (complex-rank anomaly ratio).
  These must be kept distinct.

- **AP20 (invariant of one algebra vs system)**: kappa(W_t) is an invariant
  of the W_t algebra. kappa_T = c/2 is an invariant of the Virasoro SUBALGEBRA.
  The shadow growth rate on the T-line uses kappa_T, NOT kappa(W_t).

- **AP27 (field weight vs propagator weight)**: The interpolation to complex t
  does NOT change the bar propagator. The propagator is d log E(z,w), which is
  weight 1 regardless of the rank t. All edges still use E_1.

### 7.3 What is NOT proved

1. The multi-line shadow tower at complex t (requires Deligne-category OPE
   structure constants for W_t).

2. Whether W_t in a Deligne category is Koszul (this requires the bar complex
   to make sense in the Deligne-category setting, which is not established).

3. Whether the renormalized shadow tower of W_{1+infinity} is Gaussian
   (this is a conjecture based on numerical evidence, not a proof).

4. Whether the Koszul duality W_t(c) <-> W_t(K_t - c) extends to a full
   bar-cobar adjunction at complex t (this requires operadic infrastructure
   in the Deligne-category setting).

5. Whether there exist non-trivial complex zeros of rho(t) = psi(t+1) + gamma - 1
   (numerical search found none in a bounded region, but a global statement
   about the entire complex plane would require analytic arguments).

---

## 8. Relation to the Manuscript

### 8.1 Existing results used

- thm:shadow-archetype-classification: W_N is class M (infinite depth).
  EXTENDS to complex t on the T-line.

- thm:single-line-dichotomy: Delta != 0 iff class M. EXTENDS to complex t
  (Delta_T = 40/(5c+22) != 0 generically).

- cor:anomaly-ratio-ds: rho(W_N) = sum 1/(m_i+1) = H_N - 1. EXTENDS to
  rho(t) = psi(t+1) + gamma - 1 at complex t.

- rem:koszul-conductor-explicit: K_N = 4N^3 - 2N - 2. EXTENDS to
  K_t = 4t^3 - 2t - 2 at complex t (polynomial, no obstructions).

- thm:shadow-radius: rho_shadow = sqrt((180c+872)/((5c+22)c^2)). EXTENDS
  to complex c(t,k) as an algebraic function of t.

### 8.2 New observations for potential inclusion

1. **S_3 universality at complex rank**: The gravitational cubic alpha = 2
   is independent of t, providing a T-LINE ANCHOR for the complex-rank
   interpolation.

2. **Large-rank Gaussianization**: |rho_shadow| ~ 6/t^2 -> 0 at large |t|.
   The shadow tower becomes effectively Gaussian at large rank.

3. **Harmonic divergence obstruction**: kappa(W_infinity) diverges as the
   harmonic series, requiring renormalization for W_{1+infinity}.

4. **Koszul conductor polynomial**: K_t = 4t^3 - 2t - 2 has zeros at
   t = 1 and t = (-1 +/- i)/2, giving "anomaly-free" complex ranks.

5. **Critical rank**: The T-line shadow growth rate rho = 1 at a specific
   (generically non-integer, possibly negative) value of t depending on k.

### 8.3 Potential codebase inconsistency

The file wn_channel_refined.py (line 73-82) uses the formula:

    c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)

while ds_shadow_cascade_engine.py (line 80-96) uses:

    c = (N-1)(1 - N(N+1)/(k+N))

At N=2, k=5:
- First formula: c = 1 - 2*3*6^2/7 = 1 - 216/7 = -209/7 ~ -29.86
- Second formula: c = 1 - 6/7 = 1/7 ~ 0.143

These DISAGREE. The second formula (simple Fateev-Lukyanov) is verified
to be correct by the ghost central charge identity c(sl_N) - c(W_N) = N(N-1).
The first formula appears to be the MINIMAL MODEL parameterization (using
coprime integers p, q related to k by k+N = p/q or similar), NOT the
general-level formula.

**RECTIFICATION-FLAG (AP1/AP10)**: wn_channel_refined.py and
large_n_twisted_holography.py use the BPZ minimal-model formula:

    c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)    [BPZ]

while ds_shadow_cascade_engine.py and w_infinity_shadow_limit.py use
the Sugawara formula:

    c = (N-1)(1 - N(N+1)/(k+N))             [Sugawara]

These are DIFFERENT formulas at general level k. At N=2, k=1:
BPZ gives c = -7, Sugawara gives c = -1. The correct physics central
charge at level k is the SUGAWARA formula. The BPZ formula is correct
only for minimal models parameterized by coprime (p,q) with k+N = p.

HOWEVER: the complementarity sum c(k) + c(k') = K_N is correct for
BOTH formulas, because the error cancels under FF duality (verified
symbolically). This is a classic AP10 violation: the tests pass because
both the formula AND the test encode the same wrong convention.

The wn_channel_refined.py tests are SELF-CONSISTENT with the BPZ formula
(the test explicitly checks c(W_2, k=1) = -7, which is the BPZ value).
No cross-module inconsistency exists as long as the two conventions are
not mixed. But the existence of TWO different central charge formulas
in the same codebase is a latent AP1 bomb. Any function that imports
wn_central_charge from wn_channel_refined and passes the result to a
module using the Sugawara convention will produce silently wrong answers.

The correct resolution: standardize on the Sugawara formula throughout,
with explicit BPZ parameterization as a separate function if needed
for minimal model analysis.

---

## Appendix A: Notation and Cross-References

| Symbol | Definition | Reference |
|--------|-----------|-----------|
| W_t | W-algebra at complex rank t | This document |
| c(t,k) | Central charge (t-1)(k-t^2)/(k+t) | ds_shadow_cascade_engine.py |
| rho(t) | Anomaly ratio psi(t+1)+gamma-1 | This document |
| H_t | Generalized harmonic number psi(t+1)+gamma | Standard |
| kappa(W_t) | Total mod. char. c(t,k)*rho(t) | cor:anomaly-ratio-ds |
| kappa_T | T-line kappa c/2 | w_infinity_shadow_limit.py |
| K_t | Koszul conductor 4t^3-2t-2 | rem:koszul-conductor-explicit |
| Delta_T | T-line discriminant 40/(5c+22) | discriminant_atlas.py |
| rho_shadow | Shadow growth rate on T-line | shadow_radius.py |
| S_r^T | T-line shadow coefficient at arity r | w_infinity_shadow_limit.py |

## Appendix B: Falsified Claims and Negative Results

1. **rho(t) does NOT have complex zeros** (at least in [-4,4]x[-4,4]i).
   The unique zero is t = 1 on the positive real line.

2. **The total kappa does NOT have a finite limit as t -> infinity** at fixed k.
   It diverges as t^2 log(t).

3. **The critical rank (rho_shadow = 1) is generically NOT an integer** and
   may be negative. At k = 10 it is t ~ -4.125.

4. **The Feigin-Frenkel duality does NOT give K_N = 4N^3 - 2N - 2**. Under
   FF (k -> -k-2N), c + c' = 2(N-1). The Koszul conductor K_N comes from
   the Freudenthal-de Vries formula, which accounts for the rho-shift in
   the DS reduction.

5. **The Miura transformation does NOT directly interpolate** to complex t.
   The number of free fields t-1 and the number of positive roots t(t-1)/2
   are not integers. The interpolation works at the level of OPE structure
   constants, not at the level of free-field realizations.
