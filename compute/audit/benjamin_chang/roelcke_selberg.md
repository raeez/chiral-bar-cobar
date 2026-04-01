# The Precise Spectral-Theoretic Content of epsilon^c_s

## Date: 2026-04-01
## Status: Deep analysis, falsification-first (Beilinson Principle)
## Sources: Benjamin-Chang arXiv:2208.02259 (2022), arithmetic_shadows.tex, roelcke_selberg_decomposition.py, sewing_shadow_intertwining.py, mc_spectral_measure.md

---

## 0. Executive Summary

The constrained Epstein series epsilon^c_s is the **Eisenstein spectral coefficient** of the primary-counting function Z-hat^c on M_{1,1} = SL(2,Z)\H. Its spectral-theoretic content is as follows:

1. **For Heisenberg (lattice VOAs)**: The L-function factorization of epsilon^c_s involves only holomorphic L-functions (no Maass L-functions). For V_Z: epsilon^1_s = 2 zeta(2s). The function Z-hat^c may have nonzero L^2 projections onto Maass cusp forms, but these are invisible to the constrained Epstein zeta. The distinction is between the Rankin-Selberg integral (which factors through holomorphic eigenforms) and the full L^2 spectral decomposition (which includes Maass content carrying the homotopy defect).

2. **For Virasoro at generic c**: The diagonal partition function |chi_0|^2 IS in L^2(M_{1,1}) (with polynomial growth controlled by HS-sewing), so the RS decomposition applies. The character chi_0 is NOT a modular form; |chi_0|^2 is a real-analytic automorphic function of moderate growth. The RS decomposition involves BOTH Eisenstein (continuous) and Maass (discrete) spectra. The Maass contribution is NONZERO.

3. **The poles of epsilon^c_s at s = (1+rho_n)/2**: These come from zeta(2s-1) = 0 in the functional equation factor F_c(s). The Rankin-Selberg integral I(s) is HOLOMORPHIC at the scattering poles (proved, prop:scattering-residue). The poles are in F_c(s), not in I(s); they are artifacts of the functional equation, not of the integral.

4. **Sewing-shadow intertwining**: The sewing operation connects genus-0 shadow data to genus-1 spectral data through F_1^conn = sum_r Sh_r^(1) G_r(q). For Heisenberg, the sewing determinant's RS integral against E_s yields -2(2pi)^{-(s-1)} Gamma(s-1) zeta(s-1) zeta(s) (thm:sewing-selberg-formula). The shadow tower does NOT directly control the RS decomposition; the bridge requires the sewing operation, and the sewing operation erases the scattering poles (the structural obstruction).

---

## 1. The Roelcke-Selberg Decomposition: Mathematical Framework

### 1.1 The spectral theorem on M_{1,1}

The hyperbolic Laplacian Delta = -y^2(d^2/dx^2 + d^2/dy^2) on L^2(SL(2,Z)\H, d mu) has:

- **Residual spectrum**: the constant function 1, with eigenvalue 0.
- **Continuous spectrum**: Eisenstein series E(tau, s) for s = 1/2 + it, t in R, with eigenvalue s(1-s) = 1/4 + t^2.
- **Discrete (cuspidal) spectrum**: Maass cusp forms u_j(tau) with eigenvalue lambda_j = s_j(1 - s_j) = 1/4 + t_j^2, where s_j = 1/2 + i t_j.

For any f in L^2(SL(2,Z)\H) with at most polynomial growth:

    f(tau) = <f, 1> * (3/pi)
           + (1/4pi) int_{-infty}^{infty} <f, E(., 1/2 + it)> E(tau, 1/2 + it) dt
           + sum_j <f, u_j> u_j(tau)

The Eisenstein series E(tau, s) for Re(s) > 1 is:

    E(tau, s) = (1/2) sum_{(c,d)=1} y^s / |c tau + d|^{2s}

and extends meromorphically to all s in C, with functional equation E(tau, s) = phi(s) E(tau, 1-s), where phi(s) = Lambda(1-s)/Lambda(s) is the scattering matrix and Lambda(s) = pi^{-s} Gamma(s) zeta(2s).

### 1.2 The primary-counting function

For a 2d CFT at central charge c with diagonal partition function Z(tau, tau-bar):

    Z-hat^c(tau, tau-bar) := y^{c/2} |eta(tau)|^{2c} Z(tau, tau-bar)

This strips the descendant contributions and leaves the **primary-counting data**. Explicitly, if Z = sum_i |chi_i|^2 (diagonal modular invariant), then:

    Z-hat^c = y^{c/2} |eta|^{2c} sum_i |chi_i|^2 = sum_i |y^{c/24} eta^c chi_i|^2

Each factor y^{c/24} eta^c chi_i is (morally) a generating function for primary states in the i-th representation, with the eta factor removing descendants.

### 1.3 The Benjamin-Chang construction

Benjamin-Chang define epsilon^c_s as the **Eisenstein spectral coefficient** of Z-hat^c. Concretely:

**Step 1.** Compute the zeroth Fourier mode:
    a_0(y) = int_0^1 Z-hat^c(x + iy) dx

**Step 2.** The Rankin-Selberg unfolding gives:
    I(s) := int_{SL(2,Z)\H} Z-hat^c(tau) E_s(tau) d mu(tau)
          = int_0^infty a_0(y) y^{s-2} dy

This is the Mellin transform of a_0(y).

**Step 3.** The Eisenstein spectral coefficient is:
    c_E(s) = I(s) / ||E_s||^2

(up to normalization). Benjamin-Chang identify epsilon^c_s as the Dirichlet series:
    epsilon^c_s = sum_{Delta in S} (2 Delta)^{-s}

where S is the multiset of scalar primary dimensions.

**Step 4.** The functional equation of epsilon^c_s:
    epsilon^c_{c/2 - s} = F_c(s) * epsilon^c_{c/2 + s - 1}

with

    F_c(s) = Gamma(s) Gamma(s + c/2 - 1) zeta(2s) / [pi^{2s - 1/2} Gamma(c/2 - s) Gamma(s - 1/2) zeta(2s - 1)]

This functional equation inherits poles from zeta(2s - 1) = 0 at s = (1 + rho_n)/2.

---

## 2. Investigation 1: Heisenberg (Lattice VOAs)

### 2.1 The RS decomposition for V_Z (rank 1 lattice)

The rank-1 lattice VOA V_Z has:
- Central charge c = 1
- Theta function: Theta_Z(tau) = theta_3(2 tau) = sum_{n in Z} q^{n^2}
- Partition function: Z(tau) = |theta_3(tau)|^2 / |eta(tau)|^2

The primary-counting function is:
    Z-hat^1 = y^{1/2} |Theta_Z(tau)|^2

Since Theta_Z is a modular form of weight 1/2 for Gamma_0(4), the function |Theta_Z|^2 is a real-analytic automorphic function. The key property: Z-hat^1 = y^{1/2} |Theta_Z|^2 is purely determined by the holomorphic theta function.

### 2.2 The Eisenstein coefficient

The Rankin-Selberg unfolding of |Theta_Z|^2 against E_s gives (comp:period-shadow-vz, arithmetic_shadows.tex line 738):

    epsilon^1_s = 2 zeta(2s)

This is PURELY EISENSTEIN: the constrained Epstein zeta is a single Riemann zeta function. No cusp forms contribute because S_{1/2}(Gamma_0(4)) = 0.

### 2.3 Does Z-hat^c for lattice VOAs have Maass content?

This question requires careful disambiguation between TWO different spectral decompositions.

**Decomposition A (the Rankin-Selberg integral I(s))**: The integral I(s) = int Z-hat^c E_s d mu, after RS unfolding, becomes the Mellin transform of a_0(y). For lattice VOAs, Z-hat^c = y^{c/2} |Theta_Lambda|^2, and a_0(y) = y^{c/2} sum_n |r(n)|^2 exp(-4pi n y). The Mellin transform is:

    I(s) = sum_n |r(n)|^2 (4pi n)^{-(s+c/2-1)} Gamma(s + c/2 - 1)

This is a PURE Dirichlet series (times a Gamma factor), and it factors through the Hecke decomposition of Theta_Lambda:

    Theta_Lambda = c_E E_{r/2} + sum_j c_j f_j

Each holomorphic Hecke eigenform f_j contributes L(s, f_j). NO Maass cusp forms appear in this factorization.

**Decomposition B (the L^2 spectral decomposition of Z-hat^c)**: This is the Roelcke-Selberg decomposition of Z-hat^c as a function in L^2(M_{1,1}). Here a subtle issue arises: Z-hat^c = y^{c/2} |Theta_Lambda|^2 has polynomial growth y^{c/2} as y -> infinity (since Theta_Lambda -> 1 at the cusp). For c > 0, this means Z-hat^c is NOT in L^2(M_{1,1}, d mu) (which requires square-integrability against d mu = dx dy / y^2). It IS of moderate growth, so it has a spectral decomposition in a distributional sense.

For a holomorphic cusp form f of weight k, the function y^k |f|^2 is an L^2 automorphic function. Its L^2 spectral decomposition DOES have nonzero Maass projections: <y^k |f|^2, u_j> != 0 in general. This is because the Maass cusp forms u_j form a complete orthonormal system in the cuspidal subspace of L^2, and y^k |f|^2 generically has nonzero cuspidal projection. HOWEVER, the RS integral (Decomposition A) captures the EISENSTEIN spectral coefficient, not the L^2 projections onto Maass eigenforms. The two decompositions are related but distinct.

**The precise statement for lattice VOAs**: The L-FUNCTION FACTORIZATION of epsilon^c_s involves only holomorphic L-functions and the Riemann zeta function. The L^2 spectral decomposition of Z-hat^c may have nonzero Maass projections, but these are not visible in epsilon^c_s. This is what the manuscript means by "purely Eisenstein" (comp:period-shadow-vz, comp:period-shadow-ve8, comp:period-shadow-leech). The term is slightly misleading: it refers to the L-function content, not the L^2 decomposition.

**VERIFIED COMPUTATIONALLY**: The Ising model analysis in roelcke_selberg_decomposition.py confirms: the Maass content of |chi_{1,1}|^2 + |chi_{2,1}|^2 + |chi_{1,2}|^2 is NONZERO (this is the KEY result of the computation, documented in the module header). The Ising model is a minimal model (not a lattice VOA), and its partition function is a FINITE sum of |character|^2 terms with IRRATIONAL effective conformal dimensions. The key structural result: a_0(y) ~ sum exp(-4pi Delta_i y) has exponential-decay terms that CANNOT be matched by any finite combination of power-law terms y^s + y^{1-s} (which is what a purely Eisenstein+constant decomposition would give). The Maass cusp forms, with their K-Bessel decay K_{it}(2pi n y), provide the necessary intermediate asymptotics.

**For general lattice VOAs**: the Maass L^2 projections of y^{r/2} |Theta_Lambda|^2 are nonzero, but they contribute to the "homotopy defect" part of the depth decomposition (thm:refined-shadow-spectral, d_alg >= 0), not to the arithmetic depth d_arith. The arithmetic content is fully captured by the Hecke eigenforms in the holomorphic cusp space S_{r/2}.

### 2.4 Summary for Heisenberg

| Property | Value |
|---|---|
| Z-hat^c | y^{1/2} theta_3(2tau)^2 |
| epsilon^1_s | 2 zeta(2s) |
| Eisenstein part | 2 zeta(2s) (everything) |
| Maass projection | Present as L^2 inner product, but does not contribute to epsilon^c_s |
| Cusp form content | Zero (S_{1/2}(Gamma_0(4)) = 0) |
| Shadow depth | 2 (class G, tower terminates) |

---

## 3. Investigation 2: Virasoro at Generic c

### 3.1 Is N_Vir in L^2(M_{1,1})?

The vacuum character of the Virasoro algebra at central charge c is:
    chi_0(tau) = q^{-c/24} prod_{n >= 2} (1 - q^n)^{-1}

This is NOT a modular form of any finite weight. It transforms under SL(2,Z) via the modular S-matrix, but the "modular weight" is not well-defined (the eta function contributes weight 1/2 per boson, but the null vector corrections destroy this structure).

**The key question**: is |chi_0(tau)|^2 in L^2(SL(2,Z)\H, d mu)?

**ANSWER: YES, with HS-sewing.** The manuscript proves (arithmetic_shadows.tex, line 5826):

    |chi_0(tau)|^2 = O(y^{-N}) as y -> infinity for some N

(from the HS-sewing condition, thm:general-hs-sewing). Combined with the standard polynomial growth at the cusp (y -> 0 side), this gives:

    |chi_0(tau)|^2 is an L^2_loc-automorphic function with at most polynomial growth.

**The RS decomposition APPLIES**: eq:roelcke-selberg-chi0 in arithmetic_shadows.tex (line 5836):

    |chi_0(tau)|^2 = sum_j c_j phi_j(tau)
                   + (1/4pi) int c(t) E(1/2 + it, tau) dt

where phi_j are Maass-Hecke cusp forms.

**IMPORTANT CAVEAT**: The function Z-hat^c_Vir = y^{c/2} |eta|^{2c} |chi_0|^2 is the primary-counting function, not |chi_0|^2 itself. The y^{c/2} |eta|^{2c} prefactor modifies the L^2 integrability and the spectral decomposition. The relevant object for the RS decomposition is Z-hat^c, not |chi_0|^2 alone.

For Virasoro at generic c:
    Z-hat^c_Vir(tau) = y^{c/2} |eta(tau)|^{2c} |chi_0(tau)|^2
                     = y^{c/2} |eta(tau)|^{2(c-1)} |prod_{n>=2} (1-q^n)^{-1}|^2 * |q^{-c/24} eta|^2

The cusp growth rate (def:cusp-growth-rate, prop:growth-rate-dictionary):
    alpha(Vir_c) = pi c / 12

So Z-hat^c_Vir(iy) ~ y^{c/2} exp(pi c y / 6) as y -> infinity. This GROWS exponentially at the cusp, so Z-hat^c_Vir is NOT in L^2(M_{1,1}) for c > 0. However, the RS unfolding still applies to the Mellin transform:

    I(s) = int_0^infty a_0(y) y^{s-2} dy

converges for Re(s) sufficiently large (the exponential growth at infinity is controlled by the Gamma factor in the completed L-function) and extends meromorphically.

### 3.2 The Virasoro character is quasi-modular

The Virasoro character chi_0 involves the Dedekind eta function and the null vector corrections. The product prod_{n>=2}(1-q^n)^{-1} = eta(tau)^{-1} / (1-q)^{-1} is quasi-modular (it involves E_2* through the regularized product and the modular anomaly).

**KEY DISTINCTION (AP15)**: The genus-1 propagator is E_2*(tau), which is quasi-modular, NOT holomorphic modular. Products of E_2* are quasi-modular polynomials in {E_2*, E_4, E_6}, not in {E_4, E_6}.

For the RS decomposition:
- E_2*(tau) = E_2(tau) - 3/(pi y) is NOT a modular form, but E_2*(tau) IS an almost-holomorphic modular form.
- The function |chi_0|^2 is a real-analytic automorphic function of moderate growth.
- The RS decomposition applies to real-analytic automorphic functions, not just to modular forms.

**Therefore**: The RS decomposition DOES apply to |chi_0|^2 and to Z-hat^c_Vir, provided the growth conditions are satisfied. The quasi-modular nature of chi_0 is irrelevant for the RS decomposition, which works on L^2 functions regardless of their holomorphic structure.

### 3.3 The Maass contribution for Virasoro

For Virasoro at generic irrational c, the Maass cusp form contribution to the RS decomposition of |chi_0|^2 is NONZERO.

**ARGUMENT** (from arithmetic_shadows.tex line 6029-6035):
The RS decomposition of |chi_0|^2 gives Maass-Hecke eigenforms with multiplicative Fourier coefficients. The Ramanujan bound for these eigenforms is the Selberg eigenvalue conjecture (lambda_1 >= 1/4). Best known: theta <= 7/64 (Kim-Sarnak).

**Computational evidence**: roelcke_selberg_decomposition.py verifies for the Ising model (c = 1/2) that the Maass content is nonzero. The key test (documented in the module header): the zeroth Fourier coefficient a_0(y) has exponential decay terms exp(-4pi Delta_i y) that cannot be matched by any finite combination of power-law terms y^s + y^{1-s} (which is what a purely Eisenstein decomposition would give).

**The structural reason**: for a diagonal partition function Z = sum_i |chi_i|^2 with finitely many characters (rational VOA), the function Z-hat^c is a sum of products of holomorphic functions times their conjugates. Each term |chi_i|^2 has a DISCRETE set of exponential-decay modes in y (one for each state), which are incompatible with the power-law modes of the Eisenstein series. The Maass cusp forms, with their Bessel function K_{it}(2pi ny) decay, provide the correct intermediate asymptotics.

### 3.4 For irrational c

When c is irrational, chi_0 is a single function (not part of a finite vector of characters). The function |chi_0|^2 is a real-analytic automorphic function with infinitely many exponential-decay modes (one for each primary). The RS decomposition involves:

- An Eisenstein contribution (continuous spectrum), which gives the asymptotic density of states (Cardy growth).
- A Maass contribution (discrete spectrum), which gives the oscillatory corrections to the state density.

The Maass contribution is generically NONZERO and INFINITE-DIMENSIONAL (infinitely many Maass eigenforms have nonzero projection).

---

## 4. Investigation 3: The Poles at s = (1 + rho_n)/2

### 4.1 Origin of the poles

The functional equation of epsilon^c_s (eq:constrained-epstein-fe):

    epsilon^c_{c/2 - s} = F_c(s) epsilon^c_{c/2 + s - 1}

The factor F_c(s) has poles from:
1. Gamma(c/2 - s) in the denominator: pole at s = c/2 (plus positive integers)
2. zeta(2s - 1) in the denominator: zeros at 2s - 1 = rho_n, i.e., s = (1 + rho_n)/2
3. Gamma(s - 1/2) in the denominator: pole at s = 1/2 (and negative half-integers)

### 4.2 For lattice VOAs: no Maass forms, so poles are "external"

For lattice VOAs, the RS decomposition of Z-hat^c involves only holomorphic Hecke eigenforms. The poles at s = (1+rho_n)/2 arise from the functional equation factor F_c(s), which comes from the functional equation of the Eisenstein series E(tau, s). These poles are:

- **Universal**: their locations s = (1+rho_n)/2 are the SAME for every CFT (they come from zeta, not from the CFT data).
- **The residues are CFT-dependent**: A_c(rho) (def:universal-residue-factor, eq:universal-residue) involves Gamma factors that depend on c and the zero rho.

For unimodular lattices of rank <= 24: the theta function is holomorphic (a modular form of weight r/2 for SL(2,Z)), so only holomorphic cusp forms appear, NOT Maass forms. The full arithmetic content is captured by the Hecke eigenforms in S_{r/2}(SL(2,Z)).

### 4.3 The structural obstruction (rem:structural-obstruction)

The RS integral I(s) = int Z-hat^c E_s d mu is HOLOMORPHIC at the scattering poles s = rho/2 (prop:scattering-residue, arithmetic_shadows.tex line 6885). The proof: RS unfolding replaces the integral by the Mellin transform of a_0(y), which has poles determined EXCLUSIVELY by the asymptotic behavior of a_0 at y = 0 and y = infinity. The scattering matrix phi(s) is erased by the unfolding procedure.

**Consequence**: the poles at s = (1+rho_n)/2 in the functional equation of epsilon^c_s are NOT poles of the RS integral itself. They are artifacts of expressing the functional equation in terms of the uncompleted zeta function. The completed integral has no knowledge of the zeta zeros.

This is the DECISIVE structural obstruction: the sewing/MC data constrains the spectral coefficients c(t) on the REAL spectral line (t in R), but the zeta zeros are at COMPLEX spectral parameters. No amount of algebraic constraint on the real spectral data can reach the complex scattering poles.

---

## 5. Investigation 4: Does the Shadow Tower Control the RS Decomposition?

### 5.1 The sewing-intertwining theorem

The connection between the shadow tower (genus-0 OPE data) and the RS decomposition (genus-1 spectral data) is mediated by the **sewing operation**. The intertwining theorem (sewing_shadow_intertwining.py):

    F_1^conn(q; A) = sum_{r >= 2} Sh_r^{(1)}(A) G_r(q)

where:
- Sh_r^{(1)}(A) = genus-1 shadow amplitude at arity r (from Theta_A)
- G_r(q) = r-point geometric kernel on E_tau

This decomposes the connected genus-1 free energy as a **pairing** between shadow data and geometric kernels.

### 5.2 The Heisenberg case: complete control

For Heisenberg (class G, shadow depth 2):
- Shadow tower terminates: Sh_2^{(1)} = kappa = c/2, Sh_r = 0 for r >= 3
- F_1^conn = kappa * G_2(q)
- G_2(q) = -log prod(1-q^n) / kappa

The RS decomposition:
- The sewing-Selberg formula (thm:sewing-selberg-formula): int log det(1 - K) E_s d mu = -2(2pi)^{-(s-1)} Gamma(s-1) zeta(s-1) zeta(s)
- This gives the FULL spectral content: epsilon^1_s = 2 zeta(2s)

**The shadow tower completely determines the RS decomposition for Heisenberg** because the tower terminates at kappa (a single number), and the sewing operation is exact (no higher-arity corrections).

### 5.3 The general case: partial control

For interacting theories (Virasoro, W_N, etc.):

F_1^conn = kappa G_2 + C G_3 + Q G_4 + ...

The shadow tower provides an INFINITE series of corrections to the free energy. Each correction involves a different geometric kernel G_r, and the RS decomposition of G_r involves different spectral data.

**The question**: does the shadow tower {S_r}_{r >= 2} determine the RS decomposition of F_1^conn (and hence of Z-hat^c)?

**PARTIAL ANSWER (proved)**:
- The shadow tower is determined by THREE genus-0 invariants: (kappa, alpha, S_4) via the MC equation (thm:riccati-algebraicity).
- These three invariants determine F_1^conn as a formal power series in the shadow variable t.
- The RS decomposition of F_1^conn therefore depends on the CONVERGENCE of this series and its modular properties.

**OPEN QUESTION**: Does the shadow tower, through the sewing intertwining theorem, determine the Maass cusp form projections in the RS decomposition? The answer is NO in general, for the following reason:

The shadow tower is a GENUS-0 object: it encodes the OPE data of the chiral algebra on P^1. The RS decomposition is a GENUS-1 object: it encodes the spectral theory of the partition function on the elliptic curve E_tau. The sewing operation connects the two, but the connection is not 1-to-1:

- **Forward direction (shadow -> RS)**: the shadow tower determines F_1^conn, which determines Z-hat^c (up to vacuum energy), which determines the RS decomposition. This is a CHAIN OF OPERATIONS, each of which is well-defined.

- **Backward direction (RS -> shadow)**: the RS decomposition determines Z-hat^c, which determines the primary spectrum, which constrains the OPE data. But the OPE data is NOT determined by the primary spectrum alone (different OPEs can give the same primary spectrum, at least in principle).

### 5.4 The Hecke defect as the obstruction

The precise obstruction is the **Hecke defect** (rem:prime-locality-obstruction, arithmetic_shadows.tex line 6039):

    delta_p^Hecke(A) := [d_sew, T_p] in End(g_A^mod)

where d_sew is the sewing differential and T_p is the Hecke operator.

For lattice VOAs: delta_p^Hecke = 0 (the sewing factors through the theta function, which is a Hecke eigenform). The shadow tower and the RS decomposition are in perfect correspondence.

For non-lattice theories: delta_p^Hecke is generically NONZERO. The sewing differential changes the propagator, and the Hecke translation changes the elliptic curve. These two operations do not commute because the propagator P(z,w;tau) on E_tau transforms nontrivially under isogeny.

**Prime-locality** (the vanishing or exactness of delta_p^Hecke) is the precise condition under which the shadow tower controls the arithmetic of the RS decomposition.

### 5.5 The Route C theorem

Theorem thm:route-c-propagation (arithmetic_shadows.tex line 6269) provides the bridge: IF

(a) the character-level Hecke decomposition exists (Z-hat^c decomposes into Hecke eigenfunctions), and
(b) the low-arity shadow data (kappa, alpha) are determined by the character-level data,

THEN the MC recursion propagates Hecke equivariance to ALL arities. This means the shadow tower IS compatible with the RS decomposition.

For the standard landscape: both hypotheses are satisfied (cor:route-c-standard-landscape), so **the shadow tower controls the RS decomposition for all standard families**.

For general chirally Koszul algebras: hypothesis (b) is the open step (the extraction of S_3 from character data is not established in full generality).

---

## 6. Summary and Open Questions

### 6.1 What epsilon^c_s IS (precisely)

epsilon^c_s is the Eisenstein spectral coefficient of Z-hat^c in the Roelcke-Selberg decomposition:

    Z-hat^c(tau) = <Z-hat^c, 1> (3/pi)  [residual]
                 + (1/4pi) int c_E(t) E(1/2+it, tau) dt  [Eisenstein/continuous]
                 + sum_j c_j u_j(tau)  [Maass/discrete]

Then: c_E(t) is related to epsilon^c_s by Mellin transform. Concretely,

    I(s) = int Z-hat^c E_s d mu = int_0^infty a_0(y) y^{s-2} dy

and epsilon^c_s = sum (2 Delta)^{-s} is the Dirichlet series over primary dimensions that appears when the Mellin transform is evaluated term-by-term.

### 6.2 The three spectral components of epsilon^c_s

| Component | Source | Arithmetic content |
|---|---|---|
| Eisenstein (continuous) | E(1/2+it) integral | zeta(s) zeta(s - r/2 + 1), Dirichlet L-functions |
| Holomorphic cusp forms | <Z-hat^c, F_k> (weight k) | L(s, f_j) on critical line Re(s) = k/2 |
| Maass cusp forms | <Z-hat^c, u_j> | L(s, u_j) on critical line Re(s) = 1/2 |

For lattice VOAs: only the first two rows are nonempty.
For Virasoro/W_N: all three rows contribute.

### 6.3 Open questions

1. **Quantitative Maass projection for Virasoro**: What are the Maass cusp form coefficients c_j = <Z-hat^c_Vir, u_j> as functions of c? The Ising computation (roelcke_selberg_decomposition.py) gives numerical values; a closed-form expression is unknown.

2. **Does the sewing operation diagonalize in the Maass basis?** The shadow tower intertwining F_1 = sum Sh_r G_r is a decomposition by ARITY, not by spectral type. It is unknown whether each G_r(q) has a clean decomposition into Maass eigenforms, or whether the arity decomposition and the spectral decomposition are "transverse."

3. **The quasi-modular obstruction for Route C**: The MC recursion involves the genus-1 propagator E_2*(tau), which is quasi-modular. The Hecke operators do not act as a ring homomorphism on quasi-modular forms (rem:mc-hecke-compatibility, arithmetic_shadows.tex line ~9570). Closing this gap requires understanding the Hecke action on the space of quasi-modular forms.

4. **Sewing-spectral intertwining at genus >= 2**: The RS decomposition is a genus-1 object. At genus >= 2, the "spectral decomposition" is on M_g, which is NOT a locally symmetric space (for g >= 2), so there is no Roelcke-Selberg theorem. The shadow tower produces genus-g data through the MC equation, but the spectral-theoretic framework for comparing this data to L-functions at higher genus is undeveloped.

5. **The structural obstruction revisited**: Can the RS integral be EXTENDED (not unfolded) to retain the scattering poles? The naive unfolding erases the scattering matrix. A spectral-theoretic approach that retains the scattering data would require working with the RESOLVENT of the Laplacian, not its spectral projections.

---

## 7. Falsification Notes

### 7.1 False claim: "epsilon^c_s pole at s = kappa"

The pole of epsilon^c_s at s = c/2 coincides with kappa ONLY for Virasoro (where kappa = c/2). For affine KM, kappa = dim(g)(k + h^v)/(2h^v) != c/2 = k dim(g) / (2(k+h^v)). This is documented in benjamin_chang.md section 3. Making this identification universally is AP1.

### 7.2 False claim: "The shadow tower determines the RS decomposition"

The shadow tower determines the RS decomposition ONLY when prime-locality holds. For the standard landscape, this is proved (cor:route-c-standard-landscape). For general chirally Koszul algebras, it is OPEN (the Hecke defect may be nonzero).

### 7.3 Potentially misleading claim: "purely Eisenstein" for lattice VOAs

The manuscript states (comp:period-shadow-vz): "the constrained Epstein zeta is purely Eisenstein." This is CORRECT as a statement about epsilon^c_s: the L-function factorization involves only zeta(s) zeta(s - r/2 + 1) and L(s, f_j) for holomorphic cusp forms f_j. But the FUNCTION Z-hat^c on M_{1,1}, viewed as an element of L^2 or as a distribution, generically has nonzero projections onto Maass cusp forms. The "purely Eisenstein" description refers to the L-function factorization of the Eisenstein spectral coefficient, not to the full L^2 spectral decomposition. The Maass L^2 projections carry the "homotopy defect" content (thm:refined-shadow-spectral), which is algebraic (not arithmetic) in nature. The distinction is between d_arith (captured by epsilon^c_s, measures critical lines of holomorphic L-functions) and d_alg (captured by Maass projections, measures A-infinity non-formality).

### 7.4 Verified claims

- The RS decomposition applies to |chi_0|^2 for any VOA with HS-sewing (CORRECT, proved)
- The poles at s = (1+rho)/2 are in F_c(s), not in I(s) (CORRECT, proved: prop:scattering-residue)
- The structural obstruction prevents algebraic access to zeta zeros (CORRECT, proved: rem:structural-obstruction)
- For Heisenberg: epsilon^1_s = 2 zeta(2s) (CORRECT, proved: comp:period-shadow-vz)
- The sewing-Selberg formula gives exact RS integral for log det(1-K) (CORRECT, proved: thm:sewing-selberg-formula)
